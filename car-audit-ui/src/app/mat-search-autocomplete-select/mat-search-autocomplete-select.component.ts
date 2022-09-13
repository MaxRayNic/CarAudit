import {
  AfterViewInit,
  Component,
  OnChanges,
  OnInit,
  SimpleChanges,
  ViewChild
} from '@angular/core';
import { FormControl, Validators } from '@angular/forms';
import {
  MatAutocompleteTrigger
} from '@angular/material/autocomplete';
import { merge, Observable } from 'rxjs';
import { map, startWith, switchMap, tap } from 'rxjs/operators';
import { environment } from './../../environments/environment';
import { HttpClientService } from './../../service/http-client.service';
import { RequireMatch } from './../../service/require-match';



/**
 * @title Highlight the first autocomplete option
 */
@Component({
  selector: 'app-mat-search-autocomplete-select',
  templateUrl: './mat-search-autocomplete-select.component.html',
  styleUrls: ['./mat-search-autocomplete-select.component.scss']
})
export class MatSearchAutocompleteSelectComponent implements OnInit , AfterViewInit {
  makeControl = new FormControl();
  modelControl = new FormControl('', [Validators.required, RequireMatch]);
  yearControl = new FormControl('', [Validators.required, RequireMatch]);
  mileageControl = new FormControl();
  modelExist = false;
  utility = 'Average';
  utilVal1 = 'Average';
  utilVal2 = 'Mileage';
  averageResult = null;
  predictedResult = null;
  options: string[] = Array(2022 - 1970 + 1).fill(0).map((_, i) => (1970 + i).toString());
  filteredOptionsMake: Observable<any>;
  filteredOptionsModel: Observable<any>;
  filteredOptionsYear: Observable<any>;

  showResult = false;

  @ViewChild(MatAutocompleteTrigger) trigger: MatAutocompleteTrigger;
  @ViewChild(MatAutocompleteTrigger) trigger2: MatAutocompleteTrigger;

  constructor(private httpClientService: HttpClientService){

  }

  clearResults(): void {

    console.log('cal');

    if (!this.makeControl.value){
    this.modelControl.setValue('');
    }
    if (!(this.makeControl.value && this.modelControl.value && this.yearControl.value)){
      this.averageResult = []
      this.predictedResult = null;
    }
    if (!this.mileageControl.value){
      this.predictedResult = null;
    }
    this.showResult = false;
  }



  ngOnInit(): void{
    this.filteredOptionsMake = this.makeControl.valueChanges
    .pipe(
      startWith(''),
      switchMap(val => {
        return this._filter_make(val);
      })
    );



    this.filteredOptionsYear = this.yearControl.valueChanges
    .pipe(
      startWith(''),
      switchMap(val => {
        return this._filter_make(val);
      })
    );


  }



  ngAfterViewInit(): void {
    this.trigger.panelClosingActions.subscribe(e => {
      if (!(e && e.source)) {
        this.makeControl.setValue('');
        this.trigger.closePanel();
      }
    });

    // this.trigger.panelClosingActions.subscribe(e => {
    //   if (!(e && e.source)) {
    //     this.modelControl.setValue('');
    //     this.trigger.closePanel();
    //   }
    // });

    this.trigger2.panelClosingActions.subscribe(e => {
      if (!(e && e.source)) {
        this.yearControl.setValue('');
        this.trigger2.closePanel();
        console.log('pink');

      }
    });
    console.log(this.trigger2);

  }

  private _filter_make(value: string): any {
    const filterValue = value;
    const makeEndpoint = 'make_autocomplete';
    const params = {
      make_prefix: value
    };
    const url = `${environment.apiUrl}${makeEndpoint}`;

    this.modelExist = true;
    return this.httpClientService.get_service(url, params).pipe(
      map(response => response.filter(option => {
        return option;
      })));
  }

  make_is_set(): boolean{
    return this.makeControl.value == null ? false : true;
  }

  private _filter_model(value: string): any {
    const filterValue = value;
    const modelEndpoint = 'model_autocomplete';
    const params = {
      model_prefix : value ,
      make : this.makeControl.value
    };
    const url = `${environment.apiUrl}${modelEndpoint}`;

    return this.httpClientService.get_service(url, params).pipe(
      map(response => response.filter(option => {
        return option;
      })));
  }

  private _filter_year(value: string) {
    const filterValue = value;

    const modelEndpoint = 'year_autocomplete';
    const params = {
      model : this.modelControl.value ,
      make : this.makeControl.value,
      year_prefix : value
    };
    const url = `${environment.apiUrl}${modelEndpoint}`;

    return this.httpClientService.get_service(url, params).pipe(
      map(response => response.filter(option => {
        return option;
      })));



  }
  intiateModel(event: any, item: any): void{
    this.filteredOptionsModel = this.modelControl.valueChanges
    .pipe(
      startWith(''),
      switchMap(val => {
        return this._filter_model(val);
      })
    );
  }

  intiateYear(event: any, item: any): void{
    this.filteredOptionsYear = this.yearControl.valueChanges
    .pipe(
      startWith(''),
      switchMap(val => {
        return this._filter_year(val);
      })
    );
  }

  fetchAverage(): void {

    const modelEndpoint = 'get_average_mileage_and_cost';
    const params = {
      model : this.modelControl.value ,
      make : this.makeControl.value,
      year : this.yearControl.value
    };
    const url = `${environment.apiUrl}${modelEndpoint}`;

    this.httpClientService.get_service(url, params).subscribe(
      res => {
        if (res.length > 0) {
        this.averageResult = res;
        this.showResult = true;
        }
        else{
          this.showResult = true;
          this.averageResult = [{
            model : this.modelControl.value ,
            make : this.makeControl.value,
            year : this.yearControl.value,
            average_price : 'NA',
            average_mileage : 'NA'
          }];

          }
        }
    );


  }

  fetchPrice(): void {

    const modelEndpoint = 'car_price_prediction';
    const params = {
      model : this.modelControl.value ,
      make : this.makeControl.value,
      year : this.yearControl.value,
      desired_mileage : this.mileageControl.value
    };
    const url = `${environment.apiUrl}${modelEndpoint}`;

    this.httpClientService.get_service(url, params).subscribe(


      res => {if (res[0]) {this.predictedResult = res[0]; this.showResult=true}
              else { this.predictedResult = 'NA'; this.showResult = true;
            }
      }
    );


  }


}
