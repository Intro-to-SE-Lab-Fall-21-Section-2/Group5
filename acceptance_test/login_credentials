*** Settings ***
Documentation     A test suite containing tests related to invalid login.
Suite Setup       Test Setup Actions
Suite Teardown    Test Teardown Actions
Test Setup        Go To Login Page
Test Template     Login With Invalid Credentials Should Fail
Resource          test.resource

*** Test Cases ***               USER NAME        PASSWORD
Invalid Username                 invalid          ${VALID PASSWORD}
Invalid Password                 ${VALID USER}    invalid
Invalid Username And Password    invalid          whatever
Empty Username                   ${EMPTY}         ${VALID PASSWORD}
Empty Password                   ${VALID USER}    ${EMPTY}
Empty Username And Password      ${EMPTY}         ${EMPTY}

*** Keywords ***
Login With Invalid Credentials Should Fail
    [Arguments]    ${username}    ${password}
    Input Username    ${username}
    Input Password    ${password}
    Submit Credentials
    Login Should Have Failed

Login Should Have Failed
    Location Should Be    ${ERROR URL}
    Title Should Be    Error Page
