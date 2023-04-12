*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${BROWSER}  chrome
${URL}      http://localhost:5000/

*** Test Cases ***
Example Test
    Open Browser  ${URL}  ${BROWSER}
    Maximize Browser Window
    Close Browser
