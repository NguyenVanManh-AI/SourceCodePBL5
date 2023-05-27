const axios = require('axios');
import config from '../../../config.js'
import router from './../../../router/routes' 
import useEventBus from '../../../composables/useEventBus'

let dataUser = window.localStorage.getItem('user');
let user = null;
if(dataUser){
	user = JSON.parse(dataUser);
}

export default {
	_getHeaders(){
		let headers = {};
		if(user !== null){
			headers.Authorization = 'Bearer ' + user.access_token;
		}
		return headers;
	},

	get(url){
		return new Promise( (resolve, reject) =>{ 
			axios.get(
				config.API_URL + url  , 
				{
					headers : this._getHeaders()
				}
			)
			.then( response =>{
				resolve(response.data);
			})
			.catch( error => {
				if(error.response.status == 401) this.hadleError401();
				else {
					let errors = {
						message : error.message,
						status : error.response.status
					}
					window.localStorage.setItem('error',JSON.stringify(errors));
					reject(error);
				}
			})
		});
	},
	post(url,data){
		return new Promise( (resolve, reject) =>{
			axios.post(
				config.API_URL + url, 
				data,
				{
					headers : this._getHeaders()
				}
			)
			.then( response =>{
				resolve(response.data);
			})
			.catch( error => {
				if(error.response.status == 401) this.hadleError401();
				else {
					let errors = {
						message : error.message,
						status : error.response.status
					}
					window.localStorage.setItem('error',JSON.stringify(errors));
					reject(error);
				}
			})
		})
	},
	put(url,data){
		return new Promise( (resolve, reject) =>{
			axios.put(
				config.API_URL + url, 
				data,
				{
					headers : this._getHeaders()
				}
			)
			.then( response =>{
				resolve(response.data);
			})
			.catch( error => {
				if(error.response.status == 401) this.hadleError401();
				else {
					let errors = {
						message : error.message,
						status : error.response.status
					}
					window.localStorage.setItem('error',JSON.stringify(errors));
					reject(error);
				}
			})
		})
	},
	patch(url,data){
		return new Promise( (resolve, reject) =>{
			axios.patch(
				config.API_URL + url, 
				data,
				{
					headers : this._getHeaders()
				}
			)
			.then( response =>{
				resolve(response.data);
			})
			.catch( error => {
				if(error.response.status == 401) this.hadleError401();
				else {
					let errors = {
						message : error.message,
						status : error.response.status
					}
					window.localStorage.setItem('error',JSON.stringify(errors));
					reject(error);
				}
			})
		})
	},
	delete(url){
		return new Promise( (resolve, reject) =>{
			axios.delete(
				config.API_URL + url, 
				{
					headers : this._getHeaders()
				}
			)
			.then( response =>{
				resolve(response.data);
			})
			.catch( error => {
				if(error.response.status == 401) this.hadleError401();
				else {
					let errors = {
						message : error.message,
						status : error.response.status
					}
					window.localStorage.setItem('error',JSON.stringify(errors));
					reject(error);
				}
			})
		})
	},

	hadleError401(){
		const { emitEvent } = useEventBus();
		emitEvent('eventError401','Unauthorized 401');
		window.localStorage.removeItem('user');

		setTimeout(()=>{
			router.push({name:"LoginUser"});
			window.localStorage.removeItem('error');
			window.location=window.location.href;
		}, 1500);
	}

}

