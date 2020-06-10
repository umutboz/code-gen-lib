//
// OneframeMobile iOS Api

//  Networking-Swagger Code Generate Creater 1.0
//  OneframeServiceManager.swift
//  Copyright © 2019 OneFrame Mobile - Koçsistem All rights reserved.
//

import Foundation
import Networking

class OneFrameServiceManager {
    let manager : NetworkManager
    let config = NetworkConfig.shared
    let URL = "https://oneframe-livedemo-api.azurewebsites.net"

    let  RESULT_TAG = ""
    let headerParamters : [String : String] = [
        "Accept-Language":"tr-TR"
    ]


    init() {
        manager = NetworkManager()
        manager.setNetworkLearning(learning: OneFrameLearning())
        manager.setJsonKey([])
        config.deleteAllHeaders()
        config.setURL(URL:URL)
        var _ = config.addHeader(parameters: headerParamters)
    }

    //{{request_func}}
    public func Lookups(success: @escaping (ResultModel<Lookup>) -> (),
                        fail: @escaping (ErrorModel) -> Void ) {
        manager.get("/lookups", success: success, fail: fail).fetch()
    }
    public func GetUsers(PageSize: Int, PageIndex: Int, success:  @escaping (ResultModel<String>) -> Void,
                         fail:  @escaping (ErrorModel) -> Void) {
        manager.get("/accounts?PageSize=\(PageSize)&PageIndex=\(PageIndex)",success: success, fail: fail).fetch()
    }

    public func PostUsers(user: UserPostRequest, success: @escaping (ResultModel<ApplicationUser>) -> (),
                          fail: @escaping (ErrorModel) -> Void ) {
        manager.post("/accounts",bodyParameters: user, success: success, fail: fail).fetch()
    }

    public func Search(Username: String, PageSize: Int, PageIndex: Int, success:  @escaping (ResultModel<ApplicationUser>) -> Void,
                       fail:  @escaping (ErrorModel) -> Void) {
        manager.get("/accounts/search?Username=\(Username)&PageSize=\(PageSize)&PageIndex=\(PageIndex)",success: success, fail: fail).fetch()
    }

    public func ForgotPassword(model: ForgotPasswordRequest, success: @escaping (ResultModel<String>) -> (),
                               fail: @escaping (ErrorModel) -> Void ) {
        manager.post("/accounts/forgotpassword",bodyParameters: model, success: success, fail: fail).fetch()
    }

    public func GetClaimsInRole(roleName: String, success:  @escaping (ResultModel<ClaimResponse>) -> Void,
                                fail:  @escaping (ErrorModel) -> Void) {
        manager.get("/roles/\(roleName)/claims",success: success, fail: fail).fetch()
    }

    public func AddClaimToRole(roleName: String, model: RoleClaimPostRequest, success: @escaping (ResultModel<String>) -> (),
                               fail: @escaping (ErrorModel) -> Void ) {
        manager.post("/roles/\(roleName)/claims",bodyParameters: model, success: success, fail: fail).fetch()
    }

    public func GetUsersInRoles(roleName: String, success:  @escaping (ResultModel<RoleUserResponse>) -> Void,
                                fail:  @escaping (ErrorModel) -> Void) {
        manager.get("/roles/\(roleName)/users",success: success, fail: fail).fetch()
    }

    public func GetRoles(success:  @escaping (ResultModel<String>) -> Void,
                         fail:  @escaping (ErrorModel) -> Void) {
        manager.get("/roles",success: success, fail: fail).fetch()
    }

    public func PostRoles(role: RolePostRequest, success: @escaping (ResultModel<ApplicationRole>) -> (),
                          fail: @escaping (ErrorModel) -> Void ) {
        manager.post("/roles",bodyParameters: role, success: success, fail: fail).fetch()
    }

    public func GetMenu(success:  @escaping (ResultModel<String>) -> Void,
                        fail:  @escaping (ErrorModel) -> Void) {
        manager.get("/menu",success: success, fail: fail).fetch()
    }

    public func Register(model: UserPostRequest, success: @escaping (ResultModel<LoginResponse>) -> (),
                         fail: @escaping (ErrorModel) -> Void ) {
        let token = "Bearer \(UserDefaultsManager.token() ?? "")"
        manager.post("/accounts/register",bodyParameters: model, success: success, fail: fail)
            .addHeader("Authorization", value: token)
            .fetch()
    }

    public func RemoveUserFromRole(roleName: String, username: String, success: @escaping (ResultModel<String>) -> (),
                                   fail: @escaping (ErrorModel) -> Void ) {
        manager.delete("/roles/{roleName}/users/\(username)",bodyParameters: "", success: success, fail: fail).fetch()
    }

    public func Roles(roleName: String, success:  @escaping (ResultModel<ApplicationRole>) -> Void,
                      fail:  @escaping (ErrorModel) -> Void) {
        manager.get("/roles/\(roleName)",success: success, fail: fail).fetch()
    }

    public func DeleteRoles(roleName: String, success: @escaping (ResultModel<String>) -> (),
                            fail: @escaping (ErrorModel) -> Void ) {
        manager.delete("/roles/\(roleName)",bodyParameters: "", success: success, fail: fail).fetch()
    }

    public func ResetPassword(model: ResetPasswordRequest, success: @escaping (ResultModel<String>) -> (),
                              fail: @escaping (ErrorModel) -> Void ) {
        manager.post("/accounts/resetpassword",bodyParameters: model, success: success, fail: fail).fetch()
    }

    public func Login(model: LoginRequest, success: @escaping (ResultModel<LoginResponse>) -> (),
                      fail: @escaping (ErrorModel) -> Void ) {
        manager.post("/accounts/login",bodyParameters: model, success: success, fail: fail).fetch()
    }

    public func UserGet(username: String, success:  @escaping (ResultModel<ApplicationUser>) -> Void,
                        fail:  @escaping (ErrorModel) -> Void) {
        manager.get("/accounts/\(username)",success: success, fail: fail).fetch()
    }

    public func DeleteUsers(username: String, success: @escaping (ResultModel<String>) -> (),
                            fail: @escaping (ErrorModel) -> Void ) {

        manager.delete("/accounts/\(username)",bodyParameters: "", success: success, fail: fail).fetch()
    }

    public func Patch(username: String, user: UserPatchRequest, success: @escaping (ResultModel<ApplicationUser>) -> (),
                      fail: @escaping (ErrorModel) -> Void ) {

        manager.delete("/accounts/\(username)",bodyParameters: "", success: success, fail: fail).fetch()
    }

    public func RemoveClaimFromUser(username: String, claimvalue: String, success: @escaping (ResultModel<String>) -> (),
                                    fail: @escaping (ErrorModel) -> Void ) {
        manager.delete("/accounts/{username}/claims/\(claimvalue)",bodyParameters: "", success: success, fail: fail).fetch()
    }

    public func GetClaimsInUser(username: String, success:  @escaping (ResultModel<String>) -> Void,
                                fail:  @escaping (ErrorModel) -> Void) {
        manager.get("/accounts/\(username)/claims",success: success, fail: fail).fetch()
    }

    public func AddClaimToUser(username: String, model: UserClaimPostRequest, success: @escaping (ResultModel<UserClaimPostRequest>) -> (),
                               fail: @escaping (ErrorModel) -> Void ) {
        manager.post("/accounts/\(username)/claims",bodyParameters: model, success: success, fail: fail).fetch()
    }

    public func Index(success:  @escaping (ResultModel<String>) -> Void,
                      fail:  @escaping (ErrorModel) -> Void) {
        manager.get("/install",success: success, fail: fail).fetch()
    }
}
