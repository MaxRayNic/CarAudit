import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { MatSearchAutocompleteSelectComponent } from './mat-search-autocomplete-select.component';

describe('MatSearchAutocompleteSelectComponent', () => {
  let component: MatSearchAutocompleteSelectComponent;
  let fixture: ComponentFixture<MatSearchAutocompleteSelectComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ MatSearchAutocompleteSelectComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(MatSearchAutocompleteSelectComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
