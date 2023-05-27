const axios = require('axios');
import config from '../../../config.js'
import router from './../../../router/routes' 
import useEventBus from '../../../composables/useEventBus'

let dataAdmin = window.localStorage.getItem('admin');
let admin = null;
if(dataAdmin){
	admin = JSON.parse(dataAdmin);
}

export default {
	_getHeaders(){
		let headers = {}; 
		if(admin !== null){
			headers.Authorization = 'Bearer ' + admin.access_token;
		}
		return headers;
	},

	get(url){
		return new Promise( (resolve, reject) =>{ 
			axios.get(
				config.API_URL + '/' + url  , 
				{
					headers : this._getHeaders()
				}
			)
			.then( response =>{
				resolve(response.data);
			})
			.catch( error => {
				// if(error.response.status == 404){
				// 	window.location.href = '/401';
				// }
				// if(error.response.status == 404){
				// 	window.location.href = '/404';
				// }
				// if(error.response.status == 503){
				// 	window.location.href = '/503';
				// }
				if(error.response.status == 401) this.hadleError401();
				else {
					let errors = {
						message : error.message,
						status : error.response.status
					}
					window.localStorage.setItem('error',JSON.stringify(errors));
					// router.push({name:'CompError'});
					// router.push({name:'NotFound'});
					reject(error);
				}
			})
		});
	},
	post(url,data){
		return new Promise( (resolve, reject) =>{
			axios.post(
				config.API_URL + '/' + url, 
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
				config.API_URL + '/' + url, 
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
				config.API_URL + '/' + url, 
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
				config.API_URL + '/' + url, 
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

	// Sau một thời gian thì token hết hiệu lực hoặc nếu như người dùng cố gắng hack bằng cách 
	// thêm biến admin :{} vào localSotage thì cũng vô ích vì nếu như token sau thì sẽ trả về lỗi 401 và cho về lại trang login 
	// Ta không lo lưu biến admin tại localStorage vì mỗi lần RESTful đều có yêu cầu accesss_token 
	// nếu token sai thì không làm được gì cả chính vì thế chắc chắn phải đăng nhập mới làm được 
	hadleError401(){
		const { emitEvent } = useEventBus();
		emitEvent('eventError401','Unauthorized 401');
		window.localStorage.removeItem('admin');

		setTimeout(()=>{
			router.push({name:"LoginAdmin"});
			window.localStorage.removeItem('error');
			window.location=window.location.href;
		}, 1500);
	}

	// hadleError401(){ để ntn thì mới lấy được biến router đã import còn nếu để hadleError401:function() thì không được 
	// chú ý là removeItem() chứ không phải là remove() => tránh nhầm 
}

