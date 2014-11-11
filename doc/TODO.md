# TODO NOW
 * [ ] auto wsdl generator
 * [ ] get parsed q patch from jwk
 * [ ] fix count column sort
 * [ ] incorporate mdocbuild for bin scripts
 * [ ] update readme
 * [ ] update sensor help for ask_manual_quesiton.py to describe params
 * [ ] add method to calculate total time btwn request and response
 * [ ] Deploy action
 * [ ] define package
 * [ ] AddObject
 * [ ] support options everywhere (?)

# TODO LATER
 * [ ] build "ask all questions" workflow
 * [ ] test against RT
 * [ ] test against all the different levels of user privs
 * [ ] logfile support
 * [ ] sort order? (switch to ordereddicts)
 * [ ] excel out
 * [ ] email out
 * [ ] test against demo tanium
 * [ ] Expand API examples in README.md
 * [ ] doc 3rd party modules
 * [ ] add caching

# DONE
  * 0.5.0
    * [X] better app_test
    * [X] move formatting/data transforms OUT (transforms.py?)
    * [X] REFACTOR TIME>>>>>
    * [X] json out
    * [X] refactor unittests for write_response()
    * [X] xml out
    * [X] csv out
    * [X] fix get_question_object request to map to original request
    * [X] manual query
    * [X] test on windoze
    * [X] ADD LONGER WAIT TIME FOR HIGHER est_total TO BE NICER TO API
    * [X] python wrapper scripts
    * [X] windows wrapper scripts
    * [X] unix example scripts
    * [X] test against 444 vs 443
    * [X] generalize username/password in test cases
  * 0.6.0
    * [X] re-work unit tests to be more better-er (data driven)
    * [X] re-work COUNT column hiding (need to expand testbed to have 2 or more  of one OS)
    * [X] mark parsed question as no params support (add check for [] and throw  excpetion if found)
    * [X] move XML dict grabbing stuff from soapwrap into soapresponse
    * [X] create print_sensors.py
    * [X] change get_objects into get_sensors.py/*
    * [X] test humanize_result_object on sensors single/mult/all
    * [X] support parameters in manual questions
      * [X] handle escaped commas
    * [X] add script / method to return all sensor names for discovery of manual question builder
  * 0.7.0
    * [X] support sensors filters/options/params for manual questions
    * [X] support whole question filters/options for manual questions