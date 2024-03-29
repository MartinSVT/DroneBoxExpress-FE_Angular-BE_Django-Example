import {
    HTTP_INTERCEPTORS,
    HttpEvent,
    HttpHandler,
    HttpInterceptor,
    HttpRequest,
  } from '@angular/common/http';
import { Injectable, Provider } from '@angular/core';
import { Observable, catchError } from 'rxjs';
import { Router } from '@angular/router';
import { UserMainService } from './user/user-main-service.service';


  @Injectable()
  class AppMainInter implements HttpInterceptor {
    APIkey = 'ENDPOINT';
  
    constructor(private router: Router, private userService: UserMainService) {}

    get isLoggedIn():boolean {
        return this.userService.isLogged;
      }
    get CurrentUserData():any {
        return this.userService.userData;
      }

    intercept(
      req: HttpRequest<any>,
      next: HttpHandler
    ): Observable<HttpEvent<any>> {
      if (req.url.startsWith(this.APIkey)) {
        const curToken = localStorage.getItem("token") || "";
        const tokenValue = JSON.parse(curToken)
        req = req.clone({
          url: req.url.replace(this.APIkey, ``),
          setHeaders: {Authorization: `TOKEN ${tokenValue.token}`}
        });
      }
      return next.handle(req).pipe(
        catchError((err) => {
          if (err.status === 401) {
            this.router.navigate(['/404']);
          } else {
            this.router.navigate(['/404']);
          }
          return [err];
        })
      );
    }
  }


export const AppMainInterProvider: Provider = {
    useClass: AppMainInter,
    multi: true,
    provide: HTTP_INTERCEPTORS,
}
