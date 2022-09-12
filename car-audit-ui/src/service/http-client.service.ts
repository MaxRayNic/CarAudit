import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class HttpClientService {
    constructor(private httpClient: HttpClient) { }


    get_service(url, params): Observable<any> {

      let queryParams = new HttpParams();
      for (const key of Object.keys(params)) {
        queryParams = queryParams.set(key, params[key]);
      }
      return this.httpClient.get(url, {params});
  }
}



