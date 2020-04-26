import {Injectable} from '@angular/core';
import {HttpClient,HttpHeaders} from '@angular/common/http';
import {Observable} from 'rxjs';

@Injectable({
	providedIn: 'root'
})

export class BackendApiService{
	baseUrl = "http://127.0.0.1:8000";
	httpHeaders = new HttpHeaders({
		'Content-Type':'application/json',
		'Authorization' : '',
	});
	data: any;

	constructor(private http: HttpClient){}

	// setHttpHeaders(token){
	// 	this.httpHeaders['Authorization'] = 'Token ' + token
	// }

	// authenticateUser(credentials:any): Observable<any>{
	// 	this.data=credentials;
	// 	return this.http.post(this.baseUrl + '/auth/', this.data, {headers:this.httpHeaders});
	// }

	getInitiativeList(): Observable<any>{
		return this.http.get(this.baseUrl + '/initiatives/', {headers:this.httpHeaders});
	}
	
	getInitiative(objId: any): Observable<any>{
		return this.http.get(this.baseUrl + '/initiatives/?id=' + objId, {headers:this.httpHeaders});
	}
	postInitiative(initData:any): Observable<any>{
		this.data=initData;
		return this.http.post(this.baseUrl + '/initiatives/', this.data, {headers:this.httpHeaders});
	}
}
