# Introducción a Blockchain

## _Clase 04/11/2022_


Definición Bitcoin:

> Es una moneda descentralizada que no depende de una entidad en concreto que pueda alterar su valor. Se controla a través de una cadena de bloques que verifican todos los *peers* que conforman la red.


Bitcoin core es el software que permite que la blockchain funcione. La tecnología Blockchain es del tipo DLT, pero no es la única que existe (ej: Tangle, Hashgraph). 

<br>

**Distributed Ledger Technology (DLT)**

> Consensus of replicated, shared and syncronized digital data

Características de un DLT:

- Repositorio de datos (para almacenamiento)

- Descentralizado (no hay autoridad central)

- Seguro (mediante criptografica)

- Transparente (todos los datos son publicos)

- Inmutable (no se puede cambiar el histórico)

- Autónomo (uso de smart contracts)


Características que NO tiene DLT:

- Big data (no para grandes volumenes de datos)

- Bitcoin (no solo es bitcoin)

- Real-time (hay latencia debida al minado)

- Maduro (sigue evolucionando)

- Base de datos relacional (no hay transaccionalidad)

- Un producto (hay muchas implementaciones)


Sabiendo esto, la diferencia principal entre DLT y Blockchain es que DLT engloba a blockchain.



Las primeras empresas que surgieron para transaccionar con bitcoin fueron MT.GOX (se adaptó desde la venta de cartas Magik a bitcoin) y Silk Road (marketplace anonimo). La primera hizo perder unos 800k bitcoins y quebró, y Silk Road se cerró porque se vendían muchos productos ilegales. Estos 2 hechos hicieron que bitcoin tuviera su primera bajada importante.

Después de este revés, en 2017-2018 aparecen los smart contracts, Ethereum y los ICO (Initial Coin Offering) y se produce el segundo boom de bitcoin.

En los últimos años se ha ido haciendo cada vez más popular, de manera que bancos tradicionales están empezando a sacar proyecto que implementan este tipo de tecnología.

<br>


## Criptomoneda

Definición

> Moneda digital en la que se utilizan técnicas de encriptación para regular la generación de unidades monetarias y verificar la transferencia de fondos, y que funciona independientemente de un banco central.

<p align="center">
<img src="https://www.e-zigurat.com/innovation-school/wp-content/uploads/sites/5/2019/07/grafico_crypto-vs-banking.jpg" width = 600px>
</p>

El dinero fundamentalmente es una unidad de intercambio que nos permite ejecutar ciertas acciones en nuestra sociedad. Una de sus principales características es que almacena valor, es un medio de cambio y tiene una unidad de cuenta. 


Características:

- Es un sistema que no requiere una autoridad central.

- Guarda vigilancia de la ownership de cada criptomoneda

- Define como se puede crear nuevas unidades monetarias.



Tipos de criptomonedas:

**Altcoins**: alternativas de moneda digital al dinero FIAT. Normalmente se utiliza para nombrar a todas las criptos menos a Bitcoin.


**Stablecoin**: criptomonedas diseñadas para minimizar la volatilidad en su precio

**Tokens**: son un tipo especial de token digital y representan un asset o una utilidad



Exchanges: te permiten comprar de manera centralizada criptomonedas. Esto hace que los datos de los compradores no sean anónimos. 

<br>

## CBDC


Definicion

> Son monedas emitidas por el banco central de una región y están pensadas tanto para el pago de transacciones retail como del dinero que un banco central le da a los bancos de cada país. El retail CBDC sería utilizado como extensión del cash.


**Sistema de pagos hoy en día**
<p align="center">
<img src="https://www.atlanticcouncil.org/wp-content/uploads/2020/04/Original-Figure-Canada-Payment-1024x576.png" width = 600px>
</p>


CBDC is la forma digital del monedo FIAT. Están inspirados en Bitcoin, pero son diferentes de las criptomonedas ya que estas no son emitidas por ningún estado. Puede incluso que no lleguén a implementar un DLT. Se encuentran actualmente en un estado hipotéctico haciendo algunas pruebas de concepto. 

Es probable que CBDC reemplace el dinero en efectivo en un horizonte temporal de 10-20 años. Va a tener el mismo valor que su equivalente FIAT. Se reducen tanto el coste de producción, distribución y mantenimiento, así como el fraude que tradicionalmente se hace con el dinero en efectivo.

**Usos y beneficios**
<p align="center">
<img src="https://www.bankofengland.co.uk/-/media/boe/images/paper/2020/image-3-cbdc-discussion-paper.png?h=854&la=en&w=1904&hash=E4175EC43DE61F249801A7684D66D57B2A242368
g" width = 600px>
</p>


<br>

## Como funciona Blockchain

Definicion Ethereum

> Ethereum es una plataforma de computación distribuida basada en blockhain, pública y de código abierto, y un sistema operativo con funcionalidad de contrato inteligente (scripting)

Conceptos básicos

- Hay una serie de nodos conectados entre si que ejecutan un protocolo en el lado del cliente.

- Las wallets mantienen las cuentas de los usuarios 


- Uso clave pública clave privada
    <p align="center">
    <img src="https://www.preveil.com/wp-content/uploads/2019/10/end-to-end-encryption-1024x550.png" width = 600px>
    </p>



- Uso del hash en el bloque

    <p align="center">
    <img src="https://miro.medium.com/max/1400/0*mKiuqGLo9nsfDHLo.png" width = 600px>
    </p>



**Algoritmos de Consenso**

- Proof of Work
    - No está pensado para un uso masivo por el gran consumo de energía que requiere

- Proof os Stake
    - Pones en juego tus tokens en vez de la potencia de tu ordenador

    - Se agrupa el staking de muchos usuarios para formar un nodo validador. En el caso de Ethereum se ponen 32 ethereum en stake.

    - Por poner tus tokens en riesgo para mantener la red se te da parte de las fees que gasta una persona al realizar una transferencia.



- Proof of Authority
    - Requiere todavía menos poder de computación que proof of stake

    - Funciona solo con una serie de nodos centralizados

    - Este es justo su principal problema: no es seguro ante ataques externos y es centralizado, justo lo que las criptomonedas intentan evitar



- Others (proof of weight, proof of burn, proof of capacity, etc.)



## Smart Contracts

Definición:

>Un contrato inteligente es un programa cuya ejecución es autónoma y totalmente transparente. En particular, esta ejecución no puede ser revertida y su rastro es público e inmutable


<p align="center">
<img src="https://arpitmathur.files.wordpress.com/2018/04/solidity.png" width = 400px>
</p>


El gas (o fee en la blockchain) es la tarifa que cuesta cambiar el estado de la blockchain. El precio del gas se calcula en función de las unidades de computación que cuesta (una transacción cuesta por ejemplo 21000 unidades de computación, y para un smart contract 1 millón de unidades de computación). El precio del gas por unidad de computación fluctúa con el tiempo dependiendo de lo demandada que esté la red.


**Entorno de desarrollo de smart contracts**

<https://remix.ethereum.org/>


Ejemplo de código en solidity

```js
pragma solidity >=0.7.0 <0.9.0;

/**
 * @title Storage
 * @dev Store & retrieve value in a variable
 * @custom:dev-run-script ./scripts/deploy_with_ethers.ts
 */
contract Storage {

    uint256 number;

    /**
     * @dev Store value in variable
     * @param num value to store
     */
    function store(uint256 num) public {
        number = num;
    }

    /**
     * @dev Return value 
     * @return value of 'number'
     */
    function retrieve() public view returns (uint256){
        return number;
    }
}
```



<br>


## Tokenización

Definición:
>Los criptoactivos, que también se denominan criptoactivos, son tipos especiales de fichas de moneda virtual que residen en sus propias cadenas de bloques y representan un activo o una utilidad. Lo más frecuente es que se utilicen para recaudar fondos en ventas masivas, pero también pueden utilizarse como sustituto de otras cosas.


Un NFT representa la propiedad que tú tienes sobre un activo, pero no el activo en si. Hay 2 tipos de tokens: utility tokens y security tokens. 


<p align="center">
<img src="https://www.technoloader.com/blog/wp-content/uploads/2018/04/token-development-services.jpg" width = 600px>
</p>



ERC-20: tokens fungibles. Es el más simple de los tokens fungibles.

ERC-721: tokens con un ID concreto

ERC-827: se utiliza para un tipo de security tokens




Estos estandard se definen por las funciones que tiene definidas cada uno de ellos


Beneficios de la tokenizacion

- Propiedad descentralizada

- No hay intermediarios

- Mayor liquidez

- No hay fricción

- Trazabilidad

- Hay tanto fungibles como no fungibles


Casos de uso de tokens:

- Tokenización de utilities y non-liquid objects

- Tokenización de objetos heredados (arte, real state, etc) y distribuirla entre sus herederos

- Crear y transferir rápidamente fondos de inversión (de capital privado)




Crear NFT web

<https://medium.com/gft-engineering/creating-your-own-nft-from-scratch-and-listing-it-on-opensea-8ac296cf1019>