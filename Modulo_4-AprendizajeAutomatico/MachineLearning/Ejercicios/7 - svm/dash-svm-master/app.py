"""
This app's data and plots are heavily inspired from the scikit-learn Classifier
comparison tutorial. Part of the app's code is directly taken from it. You can
find it here:
http://scikit-learn.org/stable/auto_examples/classification/plot_classifier_comparison.html

The Confusion Matrix Pie Chart format was inspired by Nicolas's Dash ROC app.
"""
import time
from textwrap import dedent
from pip._internal import main

try:
    __import__('dash')
except ImportError:
    main(['install', 'dash']) 
    
try:
    __import__('colorlover')
except ImportError:
    main(['install', 'colorlover']) 
    
    
try:
    __import__('sklearn')
except ImportError:
    main(['install', 'scikit-learn']) 

import dash
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
from dash.dependencies import Input, Output, State
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn import datasets
from sklearn.svm import SVC

import utils.dash_reusable_components as drc
from utils.figures import serve_prediction_plot, serve_roc_curve, \
    serve_pie_confusion_matrix

app = dash.Dash(__name__)
server = app.server


def generate_data(n_samples, dataset, noise):
    if dataset == 'moons':
        return datasets.make_moons(
            n_samples=n_samples,
            noise=noise,
            random_state=0
        )

    elif dataset == 'circles':
        return datasets.make_circles(
            n_samples=n_samples,
            noise=noise,
            factor=0.5,
            random_state=1
        )

    elif dataset == 'linear':
        X, y = datasets.make_classification(
            n_samples=n_samples,
            n_features=2,
            n_redundant=0,
            n_informative=2,
            random_state=2,
            n_clusters_per_class=1
        )

        rng = np.random.RandomState(2)
        X += noise * rng.uniform(size=X.shape)
        linearly_separable = (X, y)

        return linearly_separable

    else:
        raise ValueError(
            'Data type incorrectly specified. Please choose an existing '
            'dataset.')


app.layout = html.Div(children=[
    # .container class is fixed, .container.scalable is scalable
    html.Div(className="banner", children=[
        # Change App Name here
        html.Div(className='container scalable', children=[
            # Change App Name here
            html.H2(html.A(
                'Support Vector Machine (SVM) Explorer',
                href='https://github.com/plotly/dash-svm',
                style={
                    'text-decoration': 'none',
                    'color': 'inherit'
                }
            )),

            html.A(
                html.Img(src="https://s3-us-west-1.amazonaws.com/plotly-tutorials/logo/new-branding/dash-logo-by-plotly-stripe-inverted.png"),
                href='https://plot.ly/products/dash/'
            )
        ]),
    ]),

    html.Div(id='body', className='container scalable', children=[
        html.Div(className='row', children=[
            html.Div(
                id='div-graphs',
                children=dcc.Graph(
                    id='graph-sklearn-svm',
                    style={'display': 'none'}
                )
            ),

            html.Div(
                className='three columns',
                style={
                    'min-width': '24.5%',
                    'max-height': 'calc(100vh - 85px)',
                    'overflow-y': 'auto',
                    'overflow-x': 'hidden',
                },
                children=[
                    drc.Card([
                        drc.NamedDropdown(
                            name='Select Dataset',
                            id='dropdown-select-dataset',
                            options=[
                                {'label': 'Moons', 'value': 'moons'},
                                {'label': 'Linearly Separable',
                                 'value': 'linear'},
                                {'label': 'Circles', 'value': 'circles'}
                            ],
                            clearable=False,
                            searchable=False,
                            value='moons'
                        ),

                        drc.NamedSlider(
                            name='Sample Size',
                            id='slider-dataset-sample-size',
                            min=100,
                            max=500,
                            step=100,
                            marks={i: i for i in [100, 200, 300, 400, 500]},
                            value=300
                        ),

                        drc.NamedSlider(
                            name='Noise Level',
                            id='slider-dataset-noise-level',
                            min=0,
                            max=1,
                            marks={i / 10: str(i / 10) for i in
                                   range(0, 11, 2)},
                            step=0.1,
                            value=0.2,
                        ),
                    ]),

                    drc.Card([
                        drc.NamedSlider(
                            name='Threshold',
                            id='slider-threshold',
                            min=0,
                            max=1,
                            value=0.5,
                            step=0.01
                        ),

                        html.Button(
                            'Reset Threshold',
                            id='button-zero-threshold'
                        ),
                    ]),

                    drc.Card([
                        drc.NamedDropdown(
                            name='Kernel',
                            id='dropdown-svm-parameter-kernel',
                            options=[
                                {'label': 'Radial basis function (RBF)',
                                 'value': 'rbf'},
                                {'label': 'Linear', 'value': 'linear'},
                                {'label': 'Polynomial', 'value': 'poly'},
                                {'label': 'Sigmoid', 'value': 'sigmoid'}
                            ],
                            value='rbf',
                            clearable=False,
                            searchable=False
                        ),

                        drc.NamedSlider(
                            name='Cost (C)',
                            id='slider-svm-parameter-C-power',
                            min=-2,
                            max=4,
                            value=0,
                            marks={i: '{}'.format(10 ** i) for i in
                                   range(-2, 5)}
                        ),

                        drc.FormattedSlider(
                            style={'padding': '5px 10px 25px'},
                            id='slider-svm-parameter-C-coef',
                            min=1,
                            max=9,
                            value=1
                        ),

                        drc.NamedSlider(
                            name='Degree',
                            id='slider-svm-parameter-degree',
                            min=2,
                            max=10,
                            value=3,
                            step=1,
                            marks={i: i for i in range(2, 11, 2)},
                        ),

                        drc.NamedSlider(
                            name='Gamma',
                            id='slider-svm-parameter-gamma-power',
                            min=-5,
                            max=0,
                            value=-1,
                            marks={i: '{}'.format(10 ** i) for i in
                                   range(-5, 1)}
                        ),

                        drc.FormattedSlider(
                            style={'padding': '5px 10px 25px'},
                            id='slider-svm-parameter-gamma-coef',
                            min=1,
                            max=9,
                            value=5
                        ),

                        drc.NamedRadioItems(
                            name='Shrinking',
                            id='radio-svm-parameter-shrinking',
                            labelStyle={
                                'margin-right': '7px',
                                'display': 'inline-block'
                            },
                            options=[
                                {'label': ' Enabled', 'value': True},
                                {'label': ' Disabled', 'value': False},
                            ],
                            value=True,
                        ),
                    ]),

                    html.Div(
                        dcc.Markdown(dedent("""
                        [Click here](https://github.com/plotly/dash-svm) to visit the project repo, and learn about how to use the app.
                        """)),
                        style={'margin': '20px 0px', 'text-align': 'center'}
                    ),
                ]
            ),
        ]),
    ])
])


@app.callback(Output('slider-svm-parameter-gamma-coef', 'marks'),
              [Input('slider-svm-parameter-gamma-power', 'value')])
def update_slider_svm_parameter_gamma_coef(power):
    scale = 10 ** power
    return {i: str(round(i * scale, 8)) for i in range(1, 10, 2)}


@app.callback(Output('slider-svm-parameter-C-coef', 'marks'),
              [Input('slider-svm-parameter-C-power', 'value')])
def update_slider_svm_parameter_C_coef(power):
    scale = 10 ** power
    return {i: str(round(i * scale, 8)) for i in range(1, 10, 2)}


@app.callback(Output('slider-threshold', 'value'),
              [Input('button-zero-threshold', 'n_clicks')],
              [State('graph-sklearn-svm', 'figure')])
def reset_threshold_center(n_clicks, figure):
    if n_clicks:
        Z = np.array(figure['data'][0]['z'])
        value = - Z.min() / (Z.max() - Z.min())
    else:
        value = 0.4959986285375595
    return value


# Disable Sliders if kernel not in the given list
@app.callback(Output('slider-svm-parameter-degree', 'disabled'),
              [Input('dropdown-svm-parameter-kernel', 'value')])
def disable_slider_param_degree(kernel):
    return kernel != 'poly'


@app.callback(Output('slider-svm-parameter-gamma-coef', 'disabled'),
              [Input('dropdown-svm-parameter-kernel', 'value')])
def disable_slider_param_gamma_coef(kernel):
    return kernel not in ['rbf', 'poly', 'sigmoid']


@app.callback(Output('slider-svm-parameter-gamma-power', 'disabled'),
              [Input('dropdown-svm-parameter-kernel', 'value')])
def disable_slider_param_gamma_power(kernel):
    return kernel not in ['rbf', 'poly', 'sigmoid']


@app.callback(Output('div-graphs', 'children'),
              [Input('dropdown-svm-parameter-kernel', 'value'),
               Input('slider-svm-parameter-degree', 'value'),
               Input('slider-svm-parameter-C-coef', 'value'),
               Input('slider-svm-parameter-C-power', 'value'),
               Input('slider-svm-parameter-gamma-coef', 'value'),
               Input('slider-svm-parameter-gamma-power', 'value'),
               Input('dropdown-select-dataset', 'value'),
               Input('slider-dataset-noise-level', 'value'),
               Input('radio-svm-parameter-shrinking', 'value'),
               Input('slider-threshold', 'value'),
               Input('slider-dataset-sample-size', 'value')])
def update_svm_graph(kernel,
                     degree,
                     C_coef,
                     C_power,
                     gamma_coef,
                     gamma_power,
                     dataset,
                     noise,
                     shrinking,
                     threshold,
                     sample_size):
    t_start = time.time()
    h = .3  # step size in the mesh

    # Data Pre-processing
    X, y = generate_data(n_samples=sample_size, dataset=dataset, noise=noise)
    X = StandardScaler().fit_transform(X)
    X_train, X_test, y_train, y_test = \
        train_test_split(X, y, test_size=.4, random_state=42)

    x_min = X[:, 0].min() - .5
    x_max = X[:, 0].max() + .5
    y_min = X[:, 1].min() - .5
    y_max = X[:, 1].max() + .5
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))

    C = C_coef * 10 ** C_power
    gamma = gamma_coef * 10 ** gamma_power

    # Train SVM
    clf = SVC(
        C=C,
        kernel=kernel,
        degree=degree,
        gamma=gamma,
        shrinking=shrinking
    )
    clf.fit(X_train, y_train)

    # Plot the decision boundary. For that, we will assign a color to each
    # point in the mesh [x_min, x_max]x[y_min, y_max].
    if hasattr(clf, "decision_function"):
        Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
    else:
        Z = clf.predict_proba(np.c_[xx.ravel(), yy.ravel()])[:, 1]

    prediction_figure = serve_prediction_plot(
        model=clf,
        X_train=X_train,
        X_test=X_test,
        y_train=y_train,
        y_test=y_test,
        Z=Z,
        xx=xx,
        yy=yy,
        mesh_step=h,
        threshold=threshold
    )

    roc_figure = serve_roc_curve(
        model=clf,
        X_test=X_test,
        y_test=y_test
    )

    confusion_figure = serve_pie_confusion_matrix(
        model=clf,
        X_test=X_test,
        y_test=y_test,
        Z=Z,
        threshold=threshold
    )

    print(
        f"Total Time Taken: {time.time() - t_start:.3f} sec")

    return [
        html.Div(
            className='three columns',
            style={
                'min-width': '24.5%',
                'height': 'calc(100vh - 90px)',
                'margin-top': '5px',

                # Remove possibility to select the text for better UX
                'user-select': 'none',
                '-moz-user-select': 'none',
                '-webkit-user-select': 'none',
                '-ms-user-select': 'none'
            },
            children=[
                dcc.Graph(
                    id='graph-line-roc-curve',
                    style={'height': '40%'},
                    figure=roc_figure
                ),

                dcc.Graph(
                    id='graph-pie-confusion-matrix',
                    figure=confusion_figure,
                    style={'height': '60%'}
                )
            ]),

        html.Div(
            className='six columns',
            style={'margin-top': '5px'},
            children=[
                dcc.Graph(
                    id='graph-sklearn-svm',
                    figure=prediction_figure,
                    style={'height': 'calc(100vh - 90px)'}
                )
            ])
    ]


external_css = [
    # Normalize the CSS
    "https://cdnjs.cloudflare.com/ajax/libs/normalize/7.0.0/normalize.min.css",
    # Fonts
    "https://fonts.googleapis.com/css?family=Open+Sans|Roboto",
    "https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css"
]

for css in external_css:
    app.css.append_css({"external_url": css})

# Running the server
if __name__ == '__main__':
    app.run_server(debug=True)
