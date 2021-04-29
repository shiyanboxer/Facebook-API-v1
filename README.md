# Facebook-API
## Results
![Results](https://github.com/shiyanboxer/Facebook-API/blob/main/Screenshot%202020-11-03%20124459.jpg)

## Set Up Environment
1. conda create -n fbenv python=3.7 request
3. conda activate fbenv
4. conda install requests
5. pip install -e git+https://github.com/mobolic/facebook-sdk.git#egg=facebook-sdk
6. Alterative C:\Users\shiya\Anaconda3\envs\fbenv\python -m pip install <package-name>

## Facebook API Graph Explore
1. Create app
2. Generate access token - copy and paste into code
3. Request me?fields=ratings.limit(10)

## Program 
1. Import facebook and request module
2. Make a get request to the url using the access token 
3. Extract the data in json form and append to data array
4. Write the data array contents to the csv file
5. Graph the positive, negative, and neutral reviews
6. Create Flask API and Front End to visualize sentiment
