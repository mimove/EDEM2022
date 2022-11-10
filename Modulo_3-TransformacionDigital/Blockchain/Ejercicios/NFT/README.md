# How to create an NFT

To create your own NFT in the Goerli testnet blockchain follow the next steps:

<br>

## Deploy and create an NFT ERC721 Token smart contract

Tutorial followed: <https://ethereum.org/en/developers/tutorials/how-to-write-and-deploy-an-nft/>

### Creation of accounts

1. Create a free account in [Alchemy](https://auth.alchemy.com/signup)

2. Once the account is created create an app selecting Ethereum as the chain and Goerli as the network

3. If you don't have a Metamask account create it from this [link](https://metamask.io/download/) and switch to the Goerli Test Network.

4. Add Goerli Ether to your Metamask Account (Wallet) from this [link](https://goerlifaucet.com/)


### Creation of NFT project

(* WSL2 from VSCode as the terminal used in this project)

1. Check if you have Node.js and npm install by running

    ```sh
    node -v
    ```
    If it returns a version, skip to step 3

2. Install Node.js from terminal running the following

    ```sh
    sudo apt update
    sudo apt install nodejs npm
    ```

3. Create the directory of the project and initialize it

    ```sh
    mkdir my-nft
    cd my-nft
    npm init
    ```

4. Install the development environment for Ethereum [Hardhat](https://hardhat.org/hardhat-runner/docs/getting-started#overview) by running

    ```sh
    npm install --save-dev hardhat
    ```


5. Create a Hardhat project and select ```create an empty hardhat.config.js```

    ```sh
    npx hardhat
    ```

6. Copy from this repository to ```my-nft``` the folders ```contracts``` and ```scripts```

    ```sh
    cp -r <NFT repository>/contracts/ <user>/my-nft/
    cp -r <NFT repository>/scripts/ <user>/my-nft/
    ```

7. Inside the ```contracts``` folder, open MyNFT.sol and modify the variables ```<NFT name>``` and ```<NFT symbol>``` with the name and symbol that you want to give to your own NFT

    (*For an explanation of the contract visit this [link](https://ethereum.org/en/developers/tutorials/how-to-write-and-deploy-an-nft/) at step 10)

8. Install the OpenZepellin contracts library from which we inherit all the classes to create our ERC-721 standard NFT smart contract

    ```sh
    npm install @openzeppelin/contracts
    ```

    (*For an explanation of the OpenZeppelin smart contract classes visit this [link](https://ethereum.org/en/developers/tutorials/how-to-write-and-deploy-an-nft/) at step 10)

9. Link your Metamask and Alchemy accounts to your project
    
    9.1 Install the ```dotenv``` package

        ```sh
        npm install dotenv --save
        ```
    
    9.2 Copy the .env file from this repository into your folder

    ```sh
    cp <NFT repository>/.env <user>/my-nft/
    ```
    
    9.3 Modify the variables of the .env by introducing in ```API_URL``` the https of your Alchemy app, in ```PRIVATE_KEY``` the private key of your Metamask Acount and in ```API_KEY``` the key of your Alchemy app

    (*If you find any problems follow step 11 of this [link](https://ethereum.org/en/developers/tutorials/how-to-write-and-deploy-an-nft/))

10. Install Ehters.js library 

    ```sh
    npm install --save-dev @nomiclabs/hardhat-ethers ethers@^5.0.0
    ```

11. Copy from this repository hardhat.config.js into the root of the project directory
        
    ```sh
    cp <NFT respository>/hardhat.config.js <user>/my-nft/
    ```

12. Compile and deploy the contract by running from the root of the folder 

    ```sh
    npx hardhat --network goerli run scripts/deploy.js
    ```

    Something like this should be printed on the terminal

    ```sh
    Contract deployed to address: 0x4C5266cCc4b3F426965d2f51b6D910325a0E7650
    ```


13. Check that the contract has been correctly deployed by introducing the address (in the example above the address is 0x4C5266cCc4b3F426965d2f51b6D910325a0E7650) in [Goerli etherscan](https://goerli.etherscan.io/)

<br>

## Interact with the contract created by minting an NFT

Tutorial followed: <https://docs.alchemy.com/docs/how-to-mint-an-nft-from-code>

### Upload the file you want to tokenize and its metadata to [Pinata](https://www.pinata.cloud/)

1. Create an account in [Pinata](https://www.pinata.cloud/)

2. Upload a file (e.g. a png file) into Pinata

3. Copy to your directory the file ```nft-metadata.json```

    ```sh
    cp <NFT repository>/nft-metadata.json <user>/my-nft
    ```

4. Modify the file ```nft-metadata.json``` with the info of your own file from Pinata

    4.1 Change ```<author name>```, ```<img resolution>```, ```<text with description>``` and ```<name of NFT>``` with your own data

    4.2 If you don't want to provide any ```external_url``` just remove that line

    4.3 Introduce in the ```image``` the hashcode from your image in Pinate by replacing ```<img hash>``` with your own hash (e.g: https://gateway.pinata.cloud/ipfs/QmNkECnQ2KCqs8vYBx3TDKKEJ4Rg9doZoPxsXWKQRmZPDP)

5. Upload the modified ```nft-metadata.json``` to your Pinata account



### Modifying the Mint NFT Script in folder ```/scripts```

1. Modify the variable  ```<pinata metadata hash>``` from the file ```/scripts/mint-nft.js``` and put the hash of the metadata file that you've just uploaded into Pinata

2. Modify the variable ```<contract address>``` from the file ```/scripts/mint-nft.js``` and put the address of the contract that you've deployed in the first part of this tutorial


### Mint your own NFT

1. You can now mint your own NFT just by running from the root of the project directory the following command

    ```sh
    node scripts/mint-nft.js
    ```

    This should return something like:

    ```sh
    NFT Minted! Check it out at: https://goerli.etherscan.io/tx/0x06a7a06aea5d55eb6e7a0f0f17bfeaad2fb4e310de55f5a884e1b623a3fab080
    ```

2. You can view your NFT on OpenSea by searching your contract address. Check out [my NFT here](<https://testnets.opensea.io/assets/goerli/0xe154e1d863df4522e09ed0b7a48ce0ecb4782237/1>)

<br>

## Import your NFT into Metamask mobile

Very simple tutorial in this [link](<https://docs.alchemy.com/docs/how-to-view-your-nft-in-your-mobile-wallet>)