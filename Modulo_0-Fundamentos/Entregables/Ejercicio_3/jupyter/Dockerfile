FROM jupyter/base-notebook

COPY ./simpsons_notebook.ipynb /home/jovyan/work/
COPY ./requirements.txt /home/jovyan/work/

WORKDIR /home/jovyan/work/
RUN mkdir results
RUN pip install -r requirements.txt

CMD ["jupyter", "notebook", "--no-browser","--NotebookApp.token=''","--NotebookApp.password=''"]