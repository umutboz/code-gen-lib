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
 
    //{{request_func}}
public func {{function_name}}({{func_param}}success: @escaping (ResultModel<String>) -> (),
    fail: @escaping (ErrorModel) -> Void ) {
        manager.get({{query_path}}, success: success, fail: fail).fetch()
}
public func getProductList({{func_param}}success: @escaping (ResultModel<UserModel>) -> (),
    fail: @escaping (ErrorModel) -> Void ) {
        manager.get({{query_path}}, success: success, fail: fail).fetch()
}
}