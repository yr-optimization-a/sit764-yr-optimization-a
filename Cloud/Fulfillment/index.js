'use strict';

const admin =  require('firebase-admin');

// Import the Dialogflow module from the Actions on Google client library.
const {dialogflow} = require('actions-on-google');

// Import the firebase-functions package for deployment.
const functions = require('firebase-functions');

// Instantiate the Dialogflow client.
const app = dialogflow({debug: true});

const {WebhookClient} = require('dialogflow-fulfillment');

admin.initializeApp({
  credential: admin.credential.applicationDefault()
});

const firestore = admin.firestore();
const settings = {timestampsInSnapshots: true};
firestore.settings(settings);

var db = admin.firestore();

var cropDataDB = db.collection('singleCropName');
var dailyPerCapitaDB = db.collection('dailyPerCapita');

// Set the DialogflowApp object to handle the HTTPS POST request.
//exports.dialogflowFirebaseFulfillment = functions.https.onRequest(app);

process.env.DEBUG = 'dialogflow:debug'; // enables lib debugging statements

exports.dialogflowFirebaseFulfillment = functions.https.onRequest((request, response) => {
  const agent = new WebhookClient({ request, response });
  console.log('Dialogflow Request headers: ' + JSON.stringify(request.headers));
  console.log('Dialogflow Request body: ' + JSON.stringify(request.body));
  
  //const parameter = request.body.queryResult.parameters;
  
  function welcomeIntent(agent) {
    let conv = agent.conv(); 
    conv.ask('Hi, I am in welcome intent.');
  }
  
   function closeIntent(agent) {
    let conv = agent.conv(); 
    conv.close('Good Bye!');
  }
  
  function dailyPerCapitaIntent(agent)
  {
    return new Promise((resolve, reject) => {
       
        let conv = agent.conv(); 
        const countryFrom1 = agent.parameters.location;
        const countryFrom = countryFrom1.charAt(0).toUpperCase() + countryFrom1.slice(1);
        const yearFrom = parseInt(agent.parameters.year);

        console.log(countryFrom + " " + yearFrom);

        var dataFiles =  dailyPerCapitaDB
            .where('locationName', '==', countryFrom)
            .where('year', '==', yearFrom)
            .limit(1)
            .get()
            .then(doc => {
                if(doc.size > 0) {
                    let foundDoc = doc.docs[0].data();
                    console.log("Inside file exists");
                    conv.ask('The daily calorie supply of ' + foundDoc.locationName + ' in ' +
                            foundDoc.year + ' was ' + foundDoc.dailyCaloricSupply + ' ' + foundDoc.unit);
                }
                else{
                    console.log("Inside file doesnt exists");
                    conv.ask('No data found!');
                }
                let resp = agent.add(conv);
                resolve (resp);
            })
            .catch(err => {
                console.log(err);
                let resp = conv.ask('Please try again!');
                reject(resp);
            })
        ;

    });
  }
  
   function cropIntentFunc(agent)
  {
    return new Promise((resolve, reject) => {
        
        let conv = agent.conv(); 
        const cropName1 =  agent.parameters.cropData;
        var cropName = cropName1.charAt(0).toUpperCase() + cropName1.slice(1);
        var yearFrom = parseInt(agent.parameters.year);
        const countryFrom1 = agent.parameters.location;
        var countryFrom = countryFrom1.charAt(0).toUpperCase() + countryFrom1.slice(1);
        const elementType1 = agent.parameters.elementType;
        var elementType = elementType1.charAt(0).toUpperCase() + elementType1.slice(1);
        console.log(elementType+ " " + cropName + " " + countryFrom + " " + yearFrom);
        
        if((elementType && cropName) || (elementType && countryFrom) || (elementType && yearFrom) 
            || (cropName && countryFrom) || (cropName && yearFrom) || (countryFrom && yearFrom))
        {
            if(!elementType)
            {
                 elementType = conv.ask("Do you want data about Yield, Production or Harvest?");   
            }
            
            if(!cropName)
            {
                cropName = conv.ask("For which crop do you want the data?");
            }
            
            if(!countryFrom)
            {
                countryFrom = conv.ask("Which country do you want the data for?");
            }
            
            if(!yearFrom)
            {
                yearFrom = conv.ask("Which year do you want the data for?");
            }
        }
        
        var dataFiles =  cropDataDB
            .where('itemName', '==', cropName)
            .where('year', '==', yearFrom)
            .where('locationName', '==', countryFrom)
            .where('elementType', '==', elementType)
            .limit(1)
            .get()
            .then(doc => {
                if(doc.size > 0) {
                    let foundDoc = doc.docs[0].data();
                    console.log("Inside file exists");        
                    conv.ask('The '+ foundDoc.elementType +' of ' + foundDoc.itemName + ' in ' + 
                            foundDoc.locationName +' was ' + foundDoc.value + ' ' + foundDoc.unit +
                            ' for ' + foundDoc.year + '.');
                }
                else {
                    console.log("Inside file doesnt exists");
                    conv.ask('No data found!');  
                }
                let resp = agent.add(conv);
                resolve (resp);
            })
            .catch(err => {
                console.log(err);
                let resp = conv.ask('Please try again!');
                reject(resp);
            })
        ;
    });
  }
  
  let intentMap = new Map();
  intentMap.set('CropDataIntent', cropIntentFunc);
  intentMap.set('Default Welcome Intent' , welcomeIntent);
  intentMap.set('CloseIntent', closeIntent);
  intentMap.set('DailyPerCapitaIntent', dailyPerCapitaIntent);
  
  agent.handleRequest(intentMap);
});