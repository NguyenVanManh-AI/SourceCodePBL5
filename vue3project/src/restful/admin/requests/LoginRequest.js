const axios = require('axios');
import config from '../../../config.js'

export default {
	post(url,data){
		return new Promise( (resolve, reject) =>{
			axios.post(config.API_URL + '/' + url,data)
			.then( response =>{
				resolve(response.data);
			})
			.catch( error => {
				reject(error);
			})
		})
	},
    
}

