import { Injectable } from '@angular/core';
import { Post } from '../models/post.model';
import { Search } from '../models/search.model';

@Injectable({
  providedIn: 'root'
})
export class MockTestDataService {

  public mockSearchData: Search ;
  public mockPostData: Array<Post>;
  constructor() { }

  public getMockPostData() {
    this.mockPostData = [
      {
        "post_id": 1,
        "labels": "beds, oxygen",
        "post_name": "Oxygen Delivery",
        "phone_numbers": [
          "9425331581",
          "9425331581"
        ],
        "description": "Oxygen tank delivery",
        "location_city": "delhi",
        "location_area": "paharganj",
        "supporting_url": null,
        "up_votes_total": 10,
        "down_votes_total": 5,
        "date_created": "2021-04-25T12:27:35.193850+05:30"
      }
    ];
    return this.mockPostData;
  }

  public getMockSearchData() {
    this.mockSearchData =  {
      "locations": ['delhi'],
      "labels": [
          "tests",
          "food",
          "fabiflu",
          "ventilator",
          "oxygen",
          "favipiravir",
          "plasma",
          "icu",
          "remdesivir",
          "beds"
      ]
  };
    return this.mockSearchData;
  }
}
