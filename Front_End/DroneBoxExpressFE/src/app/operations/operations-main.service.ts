import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { AirportsURL, RoutesURL } from '../Environment';
import { Airport } from '../shared/interfaces';
import { tap } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class OperationsMainService {

  constructor(private myHttp: HttpClient) {}

  listRoutes() {
    return this.myHttp
      .get<any>(RoutesURL, {});
  }

  listAirports() {
    return this.myHttp
      .get<any>(AirportsURL, {});
  }

  CreateAirport(airport_name: String, lon: String, lat: String) {
    return this.myHttp.post<Airport>(
      `${AirportsURL}/`, {
        "airport_name": airport_name,
        "latitude": lat,
        "longitude": lon,
    }
    ).pipe(tap((data) => {
      console.log(data)
    }))
  }

}
