//
//
//  Networking-Swagger Code Generate Creater 1.0
//  OneframeMobileManager.swift
//  Copyright © 2020 OneFrame Mobile - Koçsistem All rights reserved.
//
 
import Foundation
import Networking
 
class OneframeMobileManager {
    let manager : NetworkManager
    let config = NetworkConfig.shared
    let URL = "{{URL}}"
     
    let  RESULT_TAG = {{"JSON_KEY"}}
    let headerParamters : [String : String] = [
        "HEADER_PARAM":"HEADER_VALUE"
    ]
     
    init() {
        manager = NetworkManager()
        manager.setJsonKey(RESULT_TAG)
        config.deleteAllHeaders()
        config.setURL(URL:URL)
        // var _ = config.addHeader(parameters: headerParamters)
    }
 
    //
	public func getTest(query:String, success: @escaping (ResultModel<String>) -> (),
	    fail: @escaping (ErrorModel) -> Void ) {
	        manager.get("api/getTest?name=query", success: success, fail: fail).fetch()
	}

	public func login(success: @escaping (ResultModel<UserModel>) -> (),
	    fail: @escaping (ErrorModel) -> Void ) {
	        manager.post("api/login", success: success, fail: fail).fetch()
	}

}