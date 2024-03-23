import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { loginURL, userDetailsURL } from '../Environment';
import { tap } from 'rxjs';



@Injectable({
  providedIn: 'root'
})
export class UserMainService {
  public guest: boolean = true;
  public user: any;

  constructor(private myHttp: HttpClient) {}

  get isLogged(): boolean {
    return !this.guest;
  }

  get userData(): any {
    return this.user
  }

  login(username: string, password: string) {
    return this.myHttp
      .post<any>(loginURL, { username, password}).pipe(tap(
        (token) => {
          console.log(token);
          localStorage.setItem("token", JSON.stringify(token));
          this.userDetaills().subscribe()
        }
        ));
  }

  userDetaills() {
    const curToken = localStorage.getItem("token") || "";
    const tokenValue = JSON.parse(curToken)
    return this.myHttp.get<any>(userDetailsURL, {
        headers: {
          'Content-Type':  'application/json',
          'Authorization': `TOKEN ${tokenValue.token}`
        }
    }).pipe(tap(
      (user) => {
        console.log(user);
        localStorage.setItem("user", JSON.stringify(user));
        this.user = user;
        this.guest = false;
      }))
  }

  logout() {
    localStorage.removeItem("token");
    localStorage.removeItem("user");
    this.user = null;
    this.guest = true
  }

}
