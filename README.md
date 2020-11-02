# Facebook-API

## Set Up Environment
1. conda create -n fbenv python=3.7 requests
2. conda activate fbenv
3. conda install requests
4. pip install -e git+https://github.com/mobolic/facebook-sdk.git#egg=facebook-sdk
5. Alterative C:\Users\shiya\Anaconda3\envs\fbenv\python -m pip install <package-name>

## Facebook API Graph Explore
1. Create app
2. Generate access token - copy and paste into code
3. Request me?fields=ratings.limit(10)

## Program 
1. Import facebook and request module
2. Make a get request to the url using the access token 
3. Extract the data in json form and append to data array
4. Write the data array contents to the csb file