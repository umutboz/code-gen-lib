//
// UserPostRequest.swift
//
// Generated by oneframemobile
// https://github.com/oneframemobile/networking-swagger-swift
//

import Networking
import Foundation


public struct UserPostRequest: Serializable {

    public var email: String?
    public var password: String
    public var phoneNumber: String?
    public var name: String?
    public var surname: String?
    

    public init(email: String?, password: String, phoneNumber: String?, name: String?, surname: String?) {
        self.email = email
        self.password = password
        self.phoneNumber = phoneNumber
        self.name = name
        self.surname = surname
    }


}

