//
//  LocationModel.swift
//  OneFrameMobileIOSTemplate
//
//  Created by Gülenay Gül on 27.02.2020.
//  Copyright © 2020 Kocsistem. All rights reserved.
//

import Foundation
import Networking

public struct GoogleLocation : Serializable {
    public var cityName : String
    public var countryName : String
    public var neighborName : String
    public var latitude : CGFloat?
    public var longitude : CGFloat?
    
    init(cityName : String, countryName : String, neighborName : String) {
        self.cityName = cityName
        self.countryName = countryName
        self.neighborName = neighborName
    }
    
}

public struct City: Serializable {
    
    public var _id: Int?
    public var name: String?
    public var counties: [County]?
    
    public init(_id: Int?, name: String?, counties: [County]?) {
        self._id = _id
        self.name = name
        self.counties = counties
    }
    
    public enum CodingKeys: String, CodingKey {
        case _id = "id"
        case name
        case counties
    }
}

public struct County: Serializable {
    
    public var _id: Int?
    public var name: String?
    public var cityId: Int?
    public var towns: [Town]?
    
    public init(_id: Int?, name: String?, cityId: Int?, towns: [Town]?) {
        self._id = _id
        self.name = name
        self.cityId = cityId
        self.towns = towns
    }
    
    public enum CodingKeys: String, CodingKey {
        case _id = "id"
        case name
        case cityId
        case towns
    }
}

public struct Town: Serializable {
    
    public var _id: Int?
    public var name: String?
    public var neighbourhoods: [Neighbourhood]?
    
    public init(_id: Int?, name: String?, neighbourhoods: [Neighbourhood]?) {
        self._id = _id
        self.name = name
        self.neighbourhoods = neighbourhoods
    }
    
    public enum CodingKeys: String, CodingKey {
        case _id = "id"
        case name
        case neighbourhoods
    }
}

public struct Neighbourhood: Serializable {
    
    public var _id: Int?
    public var name: String?
    public var zipCode: String?
    public var townId: Int?
    public var latitude : CGFloat?
    public var longitude : Double?
    
    public init(_id: Int?, name: String?, zipCode: String?, townId: Int?) {
        self._id = _id
        self.name = name
        self.zipCode = zipCode
        self.townId = townId
    }
    
    public enum CodingKeys: String, CodingKey {
        case _id = "id"
        case name
        case zipCode
        case townId
        case latitude
        case longitude
    }
}

struct LocationByCoordinateModel: Serializable {
    let cityId: Int?
    let countyId: Int?
    let neighbourhoodId: Int?
    let cityName: String?
    let countyName: String?
    let neighbourhoodName: String?
}
