//
// RolePatchRequest.swift
//
// Generated by oneframemobile
// https://github.com/oneframemobile/networking-swagger-swift
//

import Networking
import Foundation


public struct RolePatchRequest: Serializable {

    public var _description: String

    public init(_description: String) {
        self._description = _description
    }

    public enum CodingKeys: String, CodingKey { 
        case _description = "description"
    }


}

