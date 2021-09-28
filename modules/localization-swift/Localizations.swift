//
//  swift
//  Telemedic
//
//  Created by Gökhan Alp on 20.05.2020.
//  Copyright © 2020 KocSistem. All rights reserved.
//

//xcode extension
//https://developer.apple.com/documentation/xcodekit
//https://github.com/bow-swift/nef-plugin/blob/master/nef-plugin/SourceEditorExtension.swift

import Foundation
import Localize_Swift

  
    
    struct General {
        
        struct UI {
            static var tryAgainUppercased: String { get {  "General.UI.tryAgainUppercased".localized() }}
            static var okUppercased: String { get {  "General.UI.okUppercased".localized() }}
            static var continueUppercased: String { get {  "General.UI.continueUppercased".localized() }}
            static var nextUppercased: String { get {  "General.UI.nextUppercased".localized() }}
            static var save: String { get {  "General.UI.save".localized() }}
            static var followingNextUppercased: String { get {  "General.UI.followingNextUppercased".localized() }}
            static var doSearch: String { get {  "General.UI.doSearch".localized() }}
            static var opened: String { get {  "General.UI.opened".localized() }}
            static var closed: String { get {  "General.UI.closed".localized() }}
            static var close: String { get {  "General.UI.close".localized() }}
            static var turkish: String { get {  "General.UI.turkish".localized() }}
            static var english: String { get {  "General.UI.english".localized() }}
            static var countryCodes: String { get {  "General.UI.countryCodes".localized() }}
            static var add: String { get {  "General.UI.add".localized() }}
            static var yes: String { get {  "General.UI.yes".localized() }}
            static var no: String { get {  "General.UI.no".localized() }}
            static var delete: String { get {  "General.UI.delete".localized() }}
            static var edit: String { get {  "General.UI.edit".localized() }}
            static var cancel: String { get {  "General.UI.cancel".localized() }}
            static var cancel2: String { get {  "General.UI.cancel2".localized() }}
            static var choose: String { get {  "General.UI.choose".localized() }}
            static var chooseRemove: String { get {  "General.UI.chooseRemove".localized() }}
            static var tckn: String { get {  "General.UI.tckn".localized() }}
            static var passaportNo: String { get {  "General.UI.passaportNo".localized() }}
            static var retry: String { get {  "General.UI.retry".localized() }}
            static var savedInfos: String { get {  "General.UI.savedInfos".localized() }}
            static var skip: String { get {  "General.UI.skip".localized() }}
            static var changingLanguage: String { get {  "General.UI.changingLanguage".localized() }}
            static var update: String { get {  "General.UI.update".localized() }}
            static var join: String { get {  "General.UI.join".localized() }}
            static var approve: String { get {  "General.UI.approve".localized() }}
            static var returnHome: String { get {  "General.UI.returnHome".localized() }}
            static var areYouSureToDelete: String { get {  "General.UI.areYouSureToDelete".localized() }}
            static var deleteSuccess: String { get {  "General.UI.deleteSuccess".localized() }}
            static var forceUpdateText: String { get {  "General.UI.forceUpdateText".localized() }}
            static var optionalUpdateText: String { get {  "General.UI.optionalUpdateText".localized() }}
            static var exit: String { get {  "General.UI.exit".localized() }}
            static var updateFromStore: String { get {  "General.UI.updateFromStore".localized() }}
            static var done: String { get {  "General.UI.done".localized() }}
            static var orSmall: String { get { "General.UI.orSmall".localized() }}
        }
        
        struct Errors {
            static var anErrorOccured: String { get {  "General.Errors.anErrorOccured".localized() }}
            static var validateFieldsError: String { get {  "General.Errors.validateFieldsError".localized() }}
            static var failedJob: String { get {  "General.Errors.failedJob".localized() }}
            static var deviceJailBroken: String { get {  "General.Errors.deviceJailBroken".localized() }}
            
            static var responseMissingValues: String { get {  "General.Errors.responseMissingValues".localized() }}
            static var requestMissingValues: String { get {  "General.Errors.requestMissingValues".localized() }}
            static var responseModelConvertFail: String { get {  "General.Errors.responseModelConvertFail".localized() }}
            static var unkownError: String { get {  "General.Errors.unkownError".localized() }}
            static var timeout: String { get {  "General.Errors.timeout".localized() }}
            static var noConnectionError: String { get {  "General.Errors.noConnectionError".localized() }}
            static var noContent: String { get {  "General.Errors.noContent".localized() }}
            static var unAuthorized: String { get {  "General.Errors.unAuthorized".localized() }}
            static var certificatePinningError: String { get {  "General.Errors.certificatePinningError".localized() }}
            static var localizationChangeApiFetchFail: String { get {"General.Errors.localizationChangeApiFetchFail".localized() }}
            
            struct InputErrors {
                static var empty: String { get {  "General.Errors.InputErrors.empty".localized() }}
                static var emptyShort: String { get {  "General.Errors.InputErrors.emptyShort".localized() }}
                static var passwordMatch: String { get {  "General.Errors.InputErrors.passwordMatch".localized() }}
                static var phone: String { get {  "General.Errors.InputErrors.phone".localized() }}
                static var email: String { get {  "General.Errors.InputErrors.email".localized() }}
                static var tcknFail: String { get {  "General.Errors.InputErrors.tcknFail".localized() }}
                static var passwordFormatFail: String { get {  "General.Errors.InputErrors.passwordFormatFail".localized() }}
                static var emailFormatFail: String { get {  "General.Errors.InputErrors.emailFormatFail".localized() }}
                static var creditCardNoFail: String { get {  "General.Errors.InputErrors.creditCardNoFail".localized() }}
                static var phoneNoFail: String { get { "General.Errors.InputErrors.phoneNoFail".localized() }}
            }
            
            struct ComponentErrors {
                static var needsCountryForCity: String { get { "General.Errors.ComponentErrors.needsCountryForCity".localized() }}
                static var needsCityForCounty: String { get { "General.Errors.ComponentErrors.needsCityForCounty".localized() }}
            }
        }
    }
    //NSLocalizedString("incidentDetail.changeStatus.success.message", comment: "")
    struct PushNotification {
        static var changeLanguageTitle: String { get {  "PushNotification.changeLanguageTitle".localized() }}
        static var changeLanguageDescription: String { get {  "PushNotification.changeLanguageDescription".localized() }}
    }
    
    struct Pages {
        
        struct OnBoarding {
            struct OnlineAppealCreate {
                struct UI {
                    static var title: String { get {  "Pages.OnBoarding.OnlineAppealCreate.UI.title".localized() }}
                    static var description: String { get {  "Pages.OnBoarding.OnlineAppealCreate.UI.description".localized() }}
                }
            }
            
            struct OnlineExamination {
                struct UI {
                    static var title: String { get {  "Pages.OnBoarding.OnlineExamination.UI.title".localized() }}
                    static var description: String { get {  "Pages.OnBoarding.OnlineExamination.UI.description".localized() }}
                }
            }
            
            struct OnlineMeeting {
                struct UI {
                    static var title: String { get {  "Pages.OnBoarding.OnlineMeeting.UI.title".localized() }}
                    static var description: String { get {  "Pages.OnBoarding.OnlineMeeting.UI.description".localized() }}
                }
            }
            
        }
        
        struct Authentication {
            struct Login {
                struct UI {
                    static var title: String { get { return "Pages.Authentication.Login.UI.title".localized() }}
                    static var description: String { get {  "Pages.Authentication.Login.UI.description".localized() }}
                    static var password: String { get {  "Pages.Authentication.Login.UI.password".localized() }}
                    static var faq: String { get {  "Pages.Authentication.Login.UI.faq".localized() }}
                    static var forgotPassword: String { get {  "Pages.Authentication.Login.UI.forgotPassword".localized() }}
                    static var login: String { get {  "Pages.Authentication.Login.UI.login".localized() }}
                    static var dontYouHavePassword: String { get {  "Pages.Authentication.Login.UI.dontYouHavePassword".localized() }}
                    static var register: String { get {  "Pages.Authentication.Login.UI.register".localized() }}
                    static var turkishCitizen: String { get {  "Pages.Authentication.Login.UI.turkishCitizen".localized() }}
                    static var localAuthReason: String { get {  "Pages.Authentication.Login.UI.localAuthReason".localized() }}
                    static var useLocalAuthNextLogin: String { get {  "Pages.Authentication.Login.UI.useLocalAuthNextLogin".localized() }}
                }
                
                struct Errors {
                    static var token: String { get {  "Pages.Authentication.Login.Errors.token".localized() }}
                    static var localAuthNotAvaible: String { get {  "Pages.Authentication.Login.Errors.localAuthNotAvaible".localized() }}
                    static var localAuthFailed: String { get {  "Pages.Authentication.Login.Errors.localAuthFailed".localized() }}
                }
            }
            
            struct ForgotPassword {
                struct UI {
                    static var title: String { get {  "Pages.Authentication.ForgotPassword.UI.title".localized() }}
                    static var send: String { get {  "Pages.Authentication.ForgotPassword.UI.send".localized() }}
                    static var popupSuccessForgotPassword: String { get {  "Pages.Authentication.ForgotPassword.UI.popupSuccessForgotPassword".localized() }}
                    static var popupSuccessLoginButton: String { get {  "Pages.Authentication.ForgotPassword.UI.popupSuccessLoginButton".localized() }}
                }
            }
            
            struct Validation {
                struct UI {
                    static var title: String { get {  "Pages.Authentication.Validation.UI.title".localized() }}
                    static var code: String { get {  "Pages.Authentication.Validation.UI.code".localized() }}
                    static var info: String { get {  "Pages.Authentication.Validation.UI.info".localized() }}
                    static var `continue`: String { get {  "Pages.Authentication.Validation.UI.continue".localized() }};
                    static var sendAgainLeftText: String { get {  "Pages.Authentication.Validation.UI.sendAgainLeftText".localized() }};
                    static var sendAgainButton: String { get {  "Pages.Authentication.Validation.UI.sendAgainButton".localized() }};
                    static var restartSuccessPopupText: String { get {  "Pages.Authentication.Validation.UI.restartSuccessPopupText".localized() }};
                    static var validationSuccess: String { get {  "Pages.Authentication.Validation.UI.validationSuccess".localized() }};
                    static var validationSuccessToHome: String { get {  "Pages.Authentication.Validation.UI.validationSuccessToHome".localized() }};
                }
                
                struct Error {
                    static var timeout: String { get {  "Pages.Authentication.Validation.Error.timeout".localized() }}
                    static var validationFailed: String { get {  "Pages.Authentication.Validation.Error.validationFailed".localized() }}
                }
            }
            
            struct Register {
                struct First {
                    struct UI {
                        static var title: String { get {  "Pages.Authentication.Register.First.UI.title".localized() }}
                        static var birthDate: String { get {  "Pages.Authentication.Register.First.UI.birthDate".localized() }}
                        static var alreadyAvailableUser: String { get {  "Pages.Authentication.Register.First.UI.alreadyAvailableUser".localized() }}
                        static var availableButNeedsCreatePasswordUser: String { get {  "Pages.Authentication.Register.First.UI.availableButNeedsCreatePasswordUser".localized() }}
                        static var needToValidate: String { get {  "Pages.Authentication.Register.First.UI.needToValidate".localized() }}
                        static var validateAccount: String { get {  "Pages.Authentication.Register.First.UI.validateAccount".localized() }}
                        static var createPassword: String { get {  "Pages.Authentication.Register.First.UI.createPassword".localized() }}
                    }
                }
                
                struct NextRegisterDetail {
                    struct UI {
                        static var title: String { get {  "Pages.Authentication.Register.NextRegisterDetail.UI.title".localized() }}
                        static var name: String { get {  "Pages.Authentication.Register.NextRegisterDetail.UI.name".localized() }}
                        static var surname: String { get {  "Pages.Authentication.Register.NextRegisterDetail.UI.surname".localized() }}
                        static var phone: String { get {  "Pages.Authentication.Register.NextRegisterDetail.UI.phone".localized() }}
                        static var email: String { get {  "Pages.Authentication.Register.NextRegisterDetail.UI.email".localized() }}
                        static var adress: String { get {  "Pages.Authentication.Register.NextRegisterDetail.UI.adress".localized() }}
                        static var password: String { get {  "Pages.Authentication.Register.NextRegisterDetail.UI.password".localized() }}
                        static var passwordConfirmation: String { get {  "Pages.Authentication.Register.NextRegisterDetail.UI.passwordConfirmation".localized() }}
                        static var checkBoxFirstText: String { get {  "Pages.Authentication.Register.NextRegisterDetail.UI.checkBoxFirstText".localized() }}
                        static var checkBoxFirstLinkText: String { get {  "Pages.Authentication.Register.NextRegisterDetail.UI.checkBoxFirstLinkText".localized() }}
                        static var checkBoxSecondText: String { get {  "Pages.Authentication.Register.NextRegisterDetail.UI.checkBoxSecondText".localized() }}
                        static var checkBoxSecondLinkText: String { get {  "Pages.Authentication.Register.NextRegisterDetail.UI.checkBoxSecondLinkText".localized() }}
                        static var registerButton: String { get {  "Pages.Authentication.Register.NextRegisterDetail.UI.registerButton".localized() }}
                        static var gender: String { get {  "Pages.Authentication.Register.NextRegisterDetail.UI.gender".localized() }}
                        static var nation: String { get {  "Pages.Authentication.Register.NextRegisterDetail.UI.nation".localized() }}
                        static var passportEmailValidation: String { get {  "Pages.Authentication.Register.NextRegisterDetail.UI.passportEmailValidation".localized() }}
                    }
                }
            }
            
        }
        
        struct Main {
            struct Home {
                struct UI {
                    static var appointmentInfosTitle: String { get {  "Pages.Main.Home.UI.appointmentInfosTitle".localized() }}
                    static var userInfosTitle: String { get {  "Pages.Main.Home.UI.userInfosTitle".localized() }}
                    static var yearsOld: String { get {  "Pages.Main.Home.UI.yearsOld".localized() }}
                    static var backToProfile: String { get {  "Pages.Main.Home.UI.backToProfile".localized() }}
                    static var upcomingAppointments: String { get {  "Pages.Main.Home.UI.upcomingAppointments".localized() }}
                    static var appointmentWillStart: String { get {  "Pages.Main.Home.UI.appointmentWillStart".localized() }}
                    static var appointmentStarted: String { get {  "Pages.Main.Home.UI.appointmentStarted".localized() }}
                    
                    struct PhotoAdd {
                        static var addPhoto: String { get {  "Pages.Main.Home.UI.PhotoAdd.addPhoto".localized() }}
                        static var addFromGallery: String { get {  "Pages.Main.Home.UI.PhotoAdd.addFromGallery".localized() }}
                        static var addFromCamera: String { get {  "Pages.Main.Home.UI.PhotoAdd.addFromCamera".localized() }}
                    }
                    
                    struct AppointmentButtons {
                        static var createAppointment: String { get {  "Pages.Main.Home.UI.AppointmentButtons.createAppointment".localized() }}
                        static var plannedAppointments: String { get {  "Pages.Main.Home.UI.AppointmentButtons.plannedAppointments".localized() }}
                        static var passedAppointments: String { get {  "Pages.Main.Home.UI.AppointmentButtons.passedAppointments".localized() }}
                        static var waitingPayments: String { get {  "Pages.Main.Home.UI.AppointmentButtons.waitingPayments".localized() }}
                        static var plannedAppointmentsEmpty: String { get {  "Pages.Main.Home.UI.AppointmentButtons.plannedAppointmentsEmpty".localized() }}
                        static var passedAppointmentsEmpty: String { get {  "Pages.Main.Home.UI.AppointmentButtons.passedAppointmentsEmpty".localized() }}
                        static var waitingPaymentsEmpty: String { get {  "Pages.Main.Home.UI.AppointmentButtons.waitingPaymentsEmpty".localized() }}
                    }
                    
                    struct BottomUserInfos {
                        static var personalInfo: String { get {  "Pages.Main.Home.UI.BottomUserInfos.personalInfo".localized() }}
                        static var identityInfo: String { get {  "Pages.Main.Home.UI.BottomUserInfos.identityInfo".localized() }}
                        static var contactInfo: String { get {  "Pages.Main.Home.UI.BottomUserInfos.contactInfo".localized() }}
                        static var emergeCallPersonsInfo: String { get {  "Pages.Main.Home.UI.BottomUserInfos.emergeCallPersonsInfo".localized() }}
                        static var takenFromFormInfo: String { get {  "Pages.Main.Home.UI.BottomUserInfos.takenFromFormInfo".localized() }}
                        static var children: String { get {  "Pages.Main.Home.UI.BottomUserInfos.children".localized() }}
                        static var files: String { get {  "Pages.Main.Home.UI.BottomUserInfos.files".localized() }}
                    }
                    
                    struct UserInfoDetails {
                        struct PersonalInfo {
                            static var protocolNo: String { get {  "Pages.Main.Home.UI.UserInfoDetails.PersonalInfo.protocolNo".localized() }}
                            static var name: String { get {  "Pages.Main.Home.UI.UserInfoDetails.PersonalInfo.name".localized() }}
                            static var surname: String { get {  "Pages.Main.Home.UI.UserInfoDetails.PersonalInfo.surname".localized() }}
                            static var gender: String { get {  "Pages.Main.Home.UI.UserInfoDetails.PersonalInfo.gender".localized() }}
                            static var bloodGroup: String { get {  "Pages.Main.Home.UI.UserInfoDetails.PersonalInfo.bloodGroup".localized() }}
                            static var insuranceInfo: String { get {  "Pages.Main.Home.UI.UserInfoDetails.PersonalInfo.insuranceInfo".localized() }}
                            static var saveSuccess: String { get {  "Pages.Main.Home.UI.UserInfoDetails.PersonalInfo.saveSuccess".localized() }}
                        }
                        
                        struct IdentityInfo {
                            static var nation: String { get {  "Pages.Main.Home.UI.UserInfoDetails.IdentityInfo.nation".localized() }}
                            static var momName: String { get {  "Pages.Main.Home.UI.UserInfoDetails.IdentityInfo.momName".localized() }}
                            static var fatherName: String { get {  "Pages.Main.Home.UI.UserInfoDetails.IdentityInfo.fatherName".localized() }}
                            static var birthPlace: String { get {  "Pages.Main.Home.UI.UserInfoDetails.IdentityInfo.birthPlace".localized() }}
                            static var birthDate: String { get {  "Pages.Main.Home.UI.UserInfoDetails.IdentityInfo.birthDate".localized() }}
                        }
                        
                        struct ContactInfo {
                            static var phoneNo: String { get {  "Pages.Main.Home.UI.UserInfoDetails.ContactInfo.phoneNo".localized() }}
                            static var email: String { get {  "Pages.Main.Home.UI.UserInfoDetails.ContactInfo.email".localized() }}
                            static var adress: String { get {  "Pages.Main.Home.UI.UserInfoDetails.ContactInfo.adress".localized() }}
                            static var postCode: String { get {  "Pages.Main.Home.UI.UserInfoDetails.ContactInfo.postCode".localized() }}
                            static var country: String { get {  "Pages.Main.Home.UI.UserInfoDetails.ContactInfo.country".localized() }}
                            static var province: String { get {  "Pages.Main.Home.UI.UserInfoDetails.ContactInfo.province".localized() }}
                            static var district: String { get {  "Pages.Main.Home.UI.UserInfoDetails.ContactInfo.district".localized() }}
                            static var phoneAndEmail: String { get {  "Pages.Main.Home.UI.UserInfoDetails.ContactInfo.phoneAndEmail".localized() }}
                            
                            static var adressInfos: String { get {  "Pages.Main.Home.UI.UserInfoDetails.ContactInfo.adressInfos".localized() }}
                            static var adressAdd: String { get {  "Pages.Main.Home.UI.UserInfoDetails.ContactInfo.adressAdd".localized() }}
                            static var adressDetail: String { get {  "Pages.Main.Home.UI.UserInfoDetails.ContactInfo.adressDetail".localized() }}
                            static var adressEdit: String { get {  "Pages.Main.Home.UI.UserInfoDetails.ContactInfo.adressEdit".localized() }}
                            static var adressInfo: String { get {  "Pages.Main.Home.UI.UserInfoDetails.ContactInfo.adressInfo".localized() }}
                            static var adressName: String { get {  "Pages.Main.Home.UI.UserInfoDetails.ContactInfo.adressName".localized() }}
                            static var areYouSureToRemoveAdress: String { get {  "Pages.Main.Home.UI.UserInfoDetails.ContactInfo.areYouSureToRemoveAdress".localized() }}
                            static var addressAdded: String { get {  "Pages.Main.Home.UI.UserInfoDetails.ContactInfo.addressAdded".localized() }}
                            static var addressUpdated: String { get {  "Pages.Main.Home.UI.UserInfoDetails.ContactInfo.addressUpdated".localized() }}
                            static var addressRemoved: String { get {  "Pages.Main.Home.UI.UserInfoDetails.ContactInfo.addressRemoved".localized() }}
                            static var defaultAddress: String { get {  "Pages.Main.Home.UI.UserInfoDetails.ContactInfo.defaultAddress".localized() }}
                            
                            
                        }

                        struct EmergeCallInfo {
                            static var relativesOfPatient: String { get {  "Pages.Main.Home.UI.UserInfoDetails.EmergeCallInfo.relativesOfPatient".localized() }}
                            static var proximityDegree: String { get {  "Pages.Main.Home.UI.UserInfoDetails.EmergeCallInfo.proximityDegree".localized() }}
                            static var relativePhone: String { get {  "Pages.Main.Home.UI.UserInfoDetails.EmergeCallInfo.relativePhone".localized() }}
                        }
                        
                        struct Children {
                            static var childAdd: String { get {  "Pages.Main.Home.UI.UserInfoDetails.Children.childAdd".localized() }}
                            static var childEdit: String { get {  "Pages.Main.Home.UI.UserInfoDetails.Children.childEdit".localized() }}
                            static var childProfile: String { get {  "Pages.Main.Home.UI.UserInfoDetails.Children.childProfile".localized() }}
                            static var turkishCitizen: String { get {  "Pages.Main.Home.UI.UserInfoDetails.Children.turkishCitizen".localized() }}
                            static var empty: String { get {  "Pages.Main.Home.UI.UserInfoDetails.Children.empty".localized() }}
                            static var successAddChild: String { get {  "Pages.Main.Home.UI.UserInfoDetails.Children.successAddChild".localized() }}
                            static var successUpdateChild: String { get {  "Pages.Main.Home.UI.UserInfoDetails.Children.successUpdateChild".localized() }}
                        }
                    }
                    
                }
                
                struct Error {
                    struct UserInfoDetails {
                        struct Children {
                            static var childNotApproved: String { get {  "Pages.Main.Home.Error.UserInfoDetails.Children.childNotApproved".localized() }}
                        }
                    }
                }
                
            }
            
            struct Notifications {
                struct UI {
                    static var title: String { get {  "Pages.Main.Notifications.UI.title".localized() }}
                }
            }
        }
        
        struct Appointment {
            struct UI {
                
                static var title: String { get {  "Pages.Appointment.UI.title".localized() }}
                static var editTitle: String { get {  "Pages.Appointment.UI.editTitle".localized() }}
                
                struct TopSelector {
                    static var insurance: String { get {  "Pages.Appointment.UI.TopSelector.insurance".localized() }}
                    static var meetingType: String { get {  "Pages.Appointment.UI.TopSelector.meetingType".localized() }}
                    static var hospital: String { get {  "Pages.Appointment.UI.TopSelector.hospital".localized() }}
                    static var department: String { get {  "Pages.Appointment.UI.TopSelector.department".localized() }}
                    static var doctor: String { get {  "Pages.Appointment.UI.TopSelector.doctor".localized() }}
                    static var calendar: String { get {  "Pages.Appointment.UI.TopSelector.calendar".localized() }}
                    static var appointmentType: String { get {  "Pages.Appointment.UI.TopSelector.appointmentType".localized() }}
                    static var form: String { get {  "Pages.Appointment.UI.TopSelector.form".localized() }}
                    static var payment: String { get {  "Pages.Appointment.UI.TopSelector.payment".localized() }}
                    static var files: String { get {  "Pages.Appointment.UI.TopSelector.files".localized() }}
                }
                
                struct SubPages {
                    struct Insurance {
                        static var insuranceChoose: String { get {  "Pages.Appointment.UI.SubPages.Insurance.insuranceChoose".localized() }}
                        
                        static var contractedTopInfo: String { get { "Pages.Appointment.UI.SubPages.Insurance.contractedTopInfo".localized() }}
                        static var contractedBottomInfo: String { get { "Pages.Appointment.UI.SubPages.Insurance.contractedBottomInfo".localized() }}
                        
                        static var policyOptionUsePolicy: String { get {"Pages.Appointment.UI.SubPages.Insurance.policyOptionUsePolicy".localized() }}
                        static var policyOptionUseNegotiatedPrices: String { get {"Pages.Appointment.UI.SubPages.Insurance.policyOptionUseNegotiatedPrices".localized() }}
                        static var policyOptionUseIndividual: String { get {"Pages.Appointment.UI.SubPages.Insurance.policyOptionUseIndividual".localized() }}
                        static var wishToUseInsurance: String { get { "Pages.Appointment.UI.SubPages.Insurance.wishToUseInsurance".localized() }}
                    }
                    
                    struct MeetingType {
                        static var normalMeeting: String { get { "Pages.Appointment.UI.SubPages.MeetingType.normalMeeting".localized() }}
                        static var tytocareMeeting: String { get { "Pages.Appointment.UI.SubPages.MeetingType.tytocareMeeting".localized() }}
                    }
                    
                    struct MeetingPackage {
                        static var fitBitTopText: String { get { "Pages.Appointment.UI.SubPages.MeetingPackage.fitBitTopText".localized() }}
                        static var fitBitBottomText: String { get { "Pages.Appointment.UI.SubPages.MeetingPackage.fitBitBottomText".localized() }}
                        static var tytoCareTopText: String { get { "Pages.Appointment.UI.SubPages.MeetingPackage.tytoCareTopText".localized() }}
                        static var tytoCareBottomText: String { get { "Pages.Appointment.UI.SubPages.MeetingPackage.tytoCareBottomText".localized() }}
                    }
                    
                    struct Calendar {
                        static var choosedDay: String { get {  "Pages.Appointment.UI.SubPages.Calendar.choosedDay".localized() }}
                        static var fullDay: String { get {  "Pages.Appointment.UI.SubPages.Calendar.fullDay".localized() }}
                        static var editTitle: String { get {  "Pages.Appointment.UI.SubPages.Calendar.editTitle".localized() }}
                        static var editComplete: String { get {  "Pages.Appointment.UI.SubPages.Calendar.editComplete".localized() }}
                        static var needsCallCenterText: String { get {  "Pages.Appointment.UI.SubPages.Calendar.needsCallCenterText".localized() }}
                        static var needsCallCenterButton: String { get {  "Pages.Appointment.UI.SubPages.Calendar.needsCallCenterButton".localized() }}
                        static var requestCallCenterCallSuccess: String { get {  "Pages.Appointment.UI.SubPages.Calendar.requestCallCenterCallSuccess".localized() }}
                    }
                    
                    struct AppointmentType {
                        static var appointmentCreateQuestion: String { get {  "Pages.Appointment.UI.SubPages.AppointmentType.appointmentCreateQuestion".localized() }}
                        static var appointmentCreatedForDefault: String { get {  "Pages.Appointment.UI.SubPages.AppointmentType.appointmentCreatedForDefault".localized() }}
                        static var appointmentCreatedForControl: String { get {  "Pages.Appointment.UI.SubPages.AppointmentType.appointmentCreatedForControl".localized() }}
                    }
                    
                    struct Doctor {
                        static var chooseDepartment: String { get {  "Pages.Appointment.UI.SubPages.Doctor.chooseDepartment".localized() }}
                    }
                    
                    struct Form {
                        struct Shared {
                            static var quit: String { get {  "Pages.Appointment.UI.SubPages.Form.Shared.quit".localized() }}
                            static var options: String { get {  "Pages.Appointment.UI.SubPages.Form.Shared.options".localized() }}
                        }
                        
                        struct GeneralInfo {
                            static var title: String { get {  "Pages.Appointment.UI.SubPages.Form.GeneralInfo.title".localized() }}
                            static var height: String { get {  "Pages.Appointment.UI.SubPages.Form.GeneralInfo.height".localized() }}
                            static var weight: String { get {  "Pages.Appointment.UI.SubPages.Form.GeneralInfo.weight".localized() }}
                            static var vki: String { get {  "Pages.Appointment.UI.SubPages.Form.GeneralInfo.vki".localized() }}
                        }
                        
                        struct ImportantAndCronicalSickness {
                            static var title: String { get {  "Pages.Appointment.UI.SubPages.Form.ImportantAndCronicalSickness.title".localized() }}
                        }
                        
                        struct UsedMedicines {
                            static var title: String { get {  "Pages.Appointment.UI.SubPages.Form.UsedMedicines.title".localized() }}
                            static var addMedicine: String { get {  "Pages.Appointment.UI.SubPages.Form.UsedMedicines.addMedicine".localized() }}
                            static var addMedicineMedicineName: String { get {  "Pages.Appointment.UI.SubPages.Form.UsedMedicines.addMedicineMedicineName".localized() }}
                            static var addMedicineMedicineDose: String { get {  "Pages.Appointment.UI.SubPages.Form.UsedMedicines.addMedicineMedicineDose".localized() }}
                            static var addMedicineMedicineFrequency: String { get {  "Pages.Appointment.UI.SubPages.Form.UsedMedicines.addMedicineMedicineFrequency".localized() }}
                            static var addMedicineLastTakenTime: String { get {  "Pages.Appointment.UI.SubPages.Form.UsedMedicines.addMedicineLastTakenTime".localized() }}
                        }
                        
                        struct UsesBloodThinners {
                            static var title: String { get {  "Pages.Appointment.UI.SubPages.Form.UsesBloodThinners.title".localized() }}
                        }
                        
                        struct DiagnosedChronicDiseases {
                            static var title: String { get {  "Pages.Appointment.UI.SubPages.Form.DiagnosedChronicDiseases.title".localized() }}
                        }
                        
                        struct Habits {
                            static var title: String { get {  "Pages.Appointment.UI.SubPages.Form.Habits.title".localized() }}
                            static var alcoholUsage: String { get {  "Pages.Appointment.UI.SubPages.Form.Habits.alcoholUsage".localized() }}
                            static var cigaratteUsage: String { get {  "Pages.Appointment.UI.SubPages.Form.Habits.cigaratteUsage".localized() }}
                            static var drugUse: String { get {  "Pages.Appointment.UI.SubPages.Form.Habits.drugUse".localized() }}
                            static var askHowManyQuantity: String { get {  "Pages.Appointment.UI.SubPages.Form.Habits.askHowQuantity".localized() }}
                            static var askHowManyUnit: String { get {  "Pages.Appointment.UI.SubPages.Form.Habits.askHowManyUnit".localized() }}
                            static var askHowLong: String { get {  "Pages.Appointment.UI.SubPages.Form.Habits.askHowLong".localized() }}
                        }
                        
                        struct OperationHistory {
                            static var title: String { get {  "Pages.Appointment.UI.SubPages.Form.OperationHistory.title".localized() }}
                            static var operationName: String { get {  "Pages.Appointment.UI.SubPages.Form.OperationHistory.operationName".localized() }}
                            static var operationDate: String { get {  "Pages.Appointment.UI.SubPages.Form.OperationHistory.operationDate".localized() }}
                            static var operationAdd: String { get {  "Pages.Appointment.UI.SubPages.Form.OperationHistory.operationAdd".localized() }}
                        }
                        
                        struct Alergy {
                            static var title: String { get {  "Pages.Appointment.UI.SubPages.Form.Alergy.title".localized() }}
                            static var alergyAdd: String { get {  "Pages.Appointment.UI.SubPages.Form.Alergy.alergyAdd".localized() }}
                            static var medicineAlergy: String { get {  "Pages.Appointment.UI.SubPages.Form.Alergy.medicineAlergy".localized() }}
                            static var foodAlergy: String { get {  "Pages.Appointment.UI.SubPages.Form.Alergy.foodAlergy".localized() }}
                            static var otherAlergy: String { get {  "Pages.Appointment.UI.SubPages.Form.Alergy.otherAlergy".localized() }}
                        }
                        
                        struct SuddenDeath {
                            static var title: String { get {  "Pages.Appointment.UI.SubPages.Form.SuddenDeath.title".localized() }}
                            static var detail: String { get {  "Pages.Appointment.UI.SubPages.Form.SuddenDeath.detail".localized() }}
                        }
                        
                        struct Cancer {
                            static var title: String { get {  "Pages.Appointment.UI.SubPages.Form.Cancer.title".localized() }}
                        }
                    
                        struct CurrentComplaint {
                            static var title: String { get {  "Pages.Appointment.UI.SubPages.Form.CurrentComplaint.title".localized() }}
                            static var painRate: String { get {  "Pages.Appointment.UI.SubPages.Form.CurrentComplaint.painRate".localized() }}
                        }
                    }
                    
                    struct Files {
                        static var title: String { get {"Pages.Appointment.UI.SubPages.Files.title".localized() }}
                        static var fileAdd: String { get {"Pages.Appointment.UI.SubPages.Files.fileAdd".localized() }}
                        static var fileCategory: String { get {"Pages.Appointment.UI.SubPages.Files.fileCategory".localized() }}
                        static var fileName: String { get {"Pages.Appointment.UI.SubPages.Files.fileName".localized() }}
                        static var fileAddText: String { get {"Pages.Appointment.UI.SubPages.Files.fileAddText".localized() }}
                        static var fileAddedText: String { get {"Pages.Appointment.UI.SubPages.Files.fileAddedText".localized() }}
                        static var fileAddButton: String { get {"Pages.Appointment.UI.SubPages.Files.fileAddButton".localized() }}
                        static var fileUploadedSuccess: String { get {"Pages.Appointment.UI.SubPages.Files.fileUploadedSuccess".localized()}}
                        static var fileDeletedSuccess: String { get {"Pages.Appointment.UI.SubPages.Files.fileDeletedSuccess".localized()}}
                        static var filesEmptyInAppointment: String { get {"Pages.Appointment.UI.SubPages.Files.filesEmptyInAppointment".localized()}}
                        static var filesEmptyInNonAppointment: String { get {"Pages.Appointment.UI.SubPages.Files.filesEmptyInNonAppointment".localized()}}
                    }
                    
                    struct Purchase {
                        static var completeButton: String { get {  "Pages.Appointment.UI.SubPages.Purchase.completeButton".localized() }}
                        static var completeButtonForControl: String { get {  "Pages.Appointment.UI.SubPages.Purchase.completeButtonForControl".localized() }}
                        
                        static var purchaseComplete: String { get {  "Pages.Appointment.UI.SubPages.Purchase.purchaseComplete".localized() }}
                        static var appointmentCompletedForControl: String { get {  "Pages.Appointment.UI.SubPages.Purchase.appointmentCompletedForControl".localized() }}
                        
                        struct Summary {
                            static var title: String { get {  "Pages.Appointment.UI.SubPages.Purchase.Summary.title".localized() }}
                        }
                        
                        struct CardInfo {
                            static var title: String { get {  "Pages.Appointment.UI.SubPages.Purchase.CardInfo.title".localized() }}
                            static var lastUseDate: String { get {  "Pages.Appointment.UI.SubPages.Purchase.CardInfo.lastUseDate".localized() }}
                            static var cardNo: String { get {  "Pages.Appointment.UI.SubPages.Purchase.CardInfo.cardNo".localized() }}
                            static var cardOwnerName: String { get {  "Pages.Appointment.UI.SubPages.Purchase.CardInfo.cardOwnerName".localized() }}
                            static var month: String { get {  "Pages.Appointment.UI.SubPages.Purchase.CardInfo.month".localized() }}
                            static var year: String { get {  "Pages.Appointment.UI.SubPages.Purchase.CardInfo.year".localized() }}
                            static var ccv: String { get {  "Pages.Appointment.UI.SubPages.Purchase.CardInfo.ccv".localized() }}
                        }
                        
                        struct PriceInfo {
                            static var title: String { get {  "Pages.Appointment.UI.SubPages.Purchase.PriceInfo.title".localized() }}
                            static var total: String { get {  "Pages.Appointment.UI.SubPages.Purchase.PriceInfo.total".localized() }}
                            static var controlNotHaveAmount: String { get {  "Pages.Appointment.UI.SubPages.Purchase.PriceInfo.controlNotHaveAmount".localized() }}
                            
                        }
                        
                        struct Agreement {
                            static var onamForm: String { get { "Pages.Appointment.UI.SubPages.Purchase.Agreement.onamForm".localized() }}
                            static var onamFormSwitchText: String { get { "Pages.Appointment.UI.SubPages.Purchase.Agreement.onamFormSwitchText".localized() }}
                            static var distanceSaleAgreementForm: String { get { "Pages.Appointment.UI.SubPages.Purchase.Agreement.distanceSaleAgreementForm".localized() }}
                            static var distanceSaleAgreementFormSwitchText: String { get { "Pages.Appointment.UI.SubPages.Purchase.Agreement.distanceSaleAgreementFormSwitchText".localized() }}
                        }
                        
                        struct InsuranceTopInfo {
                            static var title: String { get { "Pages.Appointment.UI.SubPages.Purchase.InsuranceTopInfo.title".localized() }}
                            static var infoTop: String { get { "Pages.Appointment.UI.SubPages.Purchase.InsuranceTopInfo.infoTop".localized() }}
                            static var infoBottom: String { get { "Pages.Appointment.UI.SubPages.Purchase.InsuranceTopInfo.infoBottom".localized() }}
                        }
                        
                        struct MeetingPackageInfo {
                            static var title: String { get { "Pages.Appointment.UI.SubPages.Purchase.MeetingPackageInfo.title".localized() }}
                            static var infoTop: String { get { "Pages.Appointment.UI.SubPages.Purchase.MeetingPackageInfo.infoTop".localized() }}
                            static var infoBottom: String { get { "Pages.Appointment.UI.SubPages.Purchase.MeetingPackageInfo.infoBottom".localized() }}
                            static var infoTopLeftNothing: String { get { "Pages.Appointment.UI.SubPages.Purchase.MeetingPackageInfo.infoTopLeftNothing".localized() }}
                            static var infoBottomLeftNothing: String { get { "Pages.Appointment.UI.SubPages.Purchase.MeetingPackageInfo.infoBottomLeftNothing".localized() }}
                        }
                    }
                }
            }
            
            struct Error {
                struct ChooseAlert {
                    static var hospital: String { get {  "Pages.Appointment.Error.chooseAlert.hospital".localized() }}
                    static var doctor: String { get {  "Pages.Appointment.Error.chooseAlert.doctor".localized() }}
                    static var appointmentType: String { get {  "Pages.Appointment.Error.chooseAlert.appointmentType".localized() }}
                    static var meetingType: String { get {  "Pages.Appointment.Error.chooseAlert.meetingType".localized() }}
                }
                
                struct SubPages {
                    struct Calendar {
                        static var dayAndTimeMustSelected: String { get {  "Pages.Appointment.Error.SubPages.Calendar.dayAndTimeMustSelected".localized() }}
                        static var requestCallCenterCallFailed: String { get {  "Pages.Appointment.Error.SubPages.Calendar.requestCallCenterCallFailed".localized() }}
                        
                    }
                    
                    struct Files {
                         static var fileSize10MB: String { get {  "Pages.Appointment.Error.SubPages.Files.fileSize10MB".localized() }}
                    }
                    
                    struct Purchase {
                        static var purchaseFailed: String { get {  "Pages.Appointment.Error.SubPages.Purchase.purchaseFailed".localized() }}
                        static var mustCheckAllAgreementForms: String { get {  "Pages.Appointment.Error.SubPages.Purchase.mustCheckAllAgreementForms".localized() }}
                    }
                    
                    struct AppointmentType {
                        static var notAvaibleReservation: String { get {  "Pages.Appointment.Error.SubPages.AppointmentType.notAvaibleReservation".localized() }}
                    }
                }
                
            }
        }
        
        struct AddedAppointment {
            struct List {
                struct UI {
                    static var detail: String { get {  "Pages.AddedAppointment.List.UI.detail".localized() }}
                    static var cardHide: String { get {  "Pages.AddedAppointment.List.UI.cardHide".localized() }}
                    static var cardHideWarning: String { get {  "Pages.AddedAppointment.List.UI.cardHideWarning".localized() }}
                    static var hideComplete: String { get { "Pages.AddedAppointment.List.UI.hideComplete".localized() }}
                    static var leftTime: String { get { "Pages.AddedAppointment.List.UI.leftTime".localized() }}
                    static var continueToPayment: String { get { "Pages.AddedAppointment.List.UI.continueToPayment".localized() }}
                    static var waitingApprove: String { get {
                        "Pages.AddedAppointment.List.UI.waitingApprove".localized() }}
                    
                    static var provisionApproved: String { get {  "Pages.AddedAppointment.List.UI.provisionApproved".localized() }}
                    static var provisionDeclined: String { get {  "Pages.AddedAppointment.List.UI.provisionDeclined".localized() }}
                    static var provisionAwaiting: String { get {  "Pages.AddedAppointment.List.UI.provisionAwaiting".localized() }}
                }
                struct Error {
                    static var differentHospitalForPayment: String { get {  "Pages.AddedAppointment.List.Error.differentHospitalForPayment".localized() }}
                    static var chooseOnePaymentAtLeast: String { get {  "Pages.AddedAppointment.List.Error.chooseOnePaymentAtLeast".localized() }}
                }
            }
            
            struct Detail {
                struct UI {
                    static var title: String { get {  "Pages.AddedAppointment.Detail.UI.title".localized() }}
                    static var cellTitle: String { get {  "Pages.AddedAppointment.Detail.UI.cellTitle".localized() }}
                    static var awaitingTitle: String { get {  "Pages.AddedAppointment.Detail.UI.awaitingTitle".localized() }}
                    static var awaitingDetail: String { get {  "Pages.AddedAppointment.Detail.UI.awaitingDetail".localized() }}
                    static var completedTitle: String { get {  "Pages.AddedAppointment.Detail.UI.completedTitle".localized() }}
                    static var completedDetail: String { get {  "Pages.AddedAppointment.Detail.UI.completedDetail".localized() }}
                    static var canceledTitle: String { get {  "Pages.AddedAppointment.Detail.UI.canceledTitle".localized() }}
                    static var canceledDetail: String { get {  "Pages.AddedAppointment.Detail.UI.canceledDetail".localized() }}
                    static var edit: String { get {  "Pages.AddedAppointment.Detail.UI.edit".localized() }}
                    static var cancel: String { get {  "Pages.AddedAppointment.Detail.UI.cancel".localized() }}
                    static var areYouSureToCancel: String { get {  "Pages.AddedAppointment.Detail.UI.areYouSureToCancel".localized() }}
                    static var joinMeeting: String { get {  "Pages.AddedAppointment.Detail.UI.joinMeeting".localized() }}
                    static var tests: String { get {  "Pages.AddedAppointment.Detail.UI.tests".localized() }}
                    
                    static var tytoCareInfo: String { get {  "Pages.AddedAppointment.Detail.UI.tytoCareInfo".localized() }}
                    static var callRequestText: String { get {  "Pages.AddedAppointment.Detail.UI.callRequestText".localized() }}
                }
            }
        }
        
        struct Settings {
            struct UI {
                struct Main {
                    static var title: String { get {  "Pages.Settings.UI.Main.title".localized() }}
                    static var appointmentRemember: String { get {  "Pages.Settings.UI.Main.appointmentRemember".localized() }}
                    static var languageSettings: String { get {  "Pages.Settings.UI.Main.languageSettings".localized() }}
                    static var passwordChange: String { get {  "Pages.Settings.UI.Main.passwordChange".localized() }}
                    static var frequentlyAskedQuestions: String { get {  "Pages.Settings.UI.Main.frequentlyAskedQuestions".localized() }}
                    static var logout: String { get {  "Pages.Settings.UI.Main.logout".localized() }}
                    static var logoutAsk: String { get {  "Pages.Settings.UI.Main.logoutAsk".localized() }}
                    static var version: String { get {  "Pages.Settings.UI.Main.version".localized() }}
                    static var passwordChangeDescription: String { get {  "Pages.Settings.UI.Main.passwordChangeDescription".localized() }}
                }
                
                struct ChangePassword {
                    static var title: String { get {  "Pages.Settings.UI.ChangePassword.title".localized() }}
                    static var createPassword: String { get {  "Pages.Settings.UI.ChangePassword.createPasswordTitle".localized() }}
                    static var topText: String { get {  "Pages.Settings.UI.ChangePassword.topText".localized() }}
                    static var currentPassword: String { get {  "Pages.Settings.UI.ChangePassword.currentPassword".localized() }}
                    static var newPassword: String { get {  "Pages.Settings.UI.ChangePassword.newPassword".localized() }}
                    static var confirmPassword: String { get {  "Pages.Settings.UI.ChangePassword.confirmPassword".localized() }}
                    static var passwordChangedDone: String { get {  "Pages.Settings.UI.ChangePassword.passwordChangedDone".localized() }}
                    static var reLogin: String { get {  "Pages.Settings.UI.ChangePassword.reLogin".localized() }}
                    static var forgotPassword: String { get {  "Pages.Settings.UI.ChangePassword.forgotPassword".localized() }}
                }
                
                struct Notifications {
                    static var title: String { get {  "Pages.Settings.UI.Notifications.title".localized() }}
                    static var sms: String { get {  "Pages.Settings.UI.Notifications.sms".localized() }}
                    static var email: String { get {  "Pages.Settings.UI.Notifications.email".localized() }}
                    static var pushNotification: String { get {  "Pages.Settings.UI.Notifications.pushNotification".localized() }}
                }
                
                struct FAQ {
                    static var title: String { get {  "Pages.Settings.UI.FAQ.title".localized() }}
                }
            }
        }
        
        struct Meeting {
            struct UI {
                static var meeting: String { get {  "Pages.Meeting.UI.meeting".localized() }}
                static var join: String { get {  "Pages.Meeting.UI.join".localized() }}
                static var noUserAvaibleText: String { get {  "Pages.Meeting.UI.noUserAvaibleText".localized() }}
                static var speakerChooseTitle: String { get {  "Pages.Meeting.UI.speakerChooseTitle".localized() }}
                static var speakerChooseHandset: String { get {  "Pages.Meeting.UI.speakerChooseHandset".localized() }}
                static var speakerChooseSpeaker: String { get {  "Pages.Meeting.UI.speakerChooseSpeaker".localized() }}
                static var speakerChooseCloseSound: String { get {  "Pages.Meeting.UI.speakerChooseCloseSound".localized() }}
            }
            
            struct Error {
                static var joinFailedError: String { get { "Pages.Meeting.Error.joinFailedError".localized() }}
                static var unableToJoin: String { get { "Pages.Meeting.Error.unableToJoin".localized() }}
                static var joinFailedNotGranted: String { get { "Pages.Meeting.Error.joinFailedNotGranted".localized() }}
            }
        }
        
    }
    
    struct Components {
        struct Insurance {
            struct UI {
                static var title: String { get {  "Components.Insurance.UI.title".localized() }}
                static var policyChooseTitle: String { get {  "Components.Insurance.UI.policyChooseTitle".localized() }}
                static var insuranceChooseTitle: String { get {  "Components.Insurance.UI.insuranceChooseTitle".localized() }}
            }
            
            struct Errors {
                static var pleaseSelectInsurance: String { get { "Components.Insurance.Errors.pleaseSelectInsurance".localized() }}
            }
        }
    }
    
    struct Shared {
        struct MeetingType {
            struct UI {
                static var normalPackage: String { get { "Shared.MeetingType.UI.normalPackage".localized() }}
                static var tytocareMeeting: String { get { "Shared.MeetingType.UI.tytocareMeeting".localized() }}
                static var tytocarePackage: String { get { "Shared.MeetingType.UI.tytocarePackage".localized() }}
                static var tytocareFitbitPackage: String { get { "Shared.MeetingType.UI.tytocareFitbitPackage".localized() }}
                static var fitbitPackage: String { get { "Shared.MeetingType.UI.fitbitPackage".localized() }}
                
                static var meetingTextAdd: String { get { "Shared.MeetingType.UI.meetingTextAdd".localized() }}
            }
        }
    }
}
