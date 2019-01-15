# Generated by zerotest
from __future__ import unicode_literals
from zerotest.request import Request
from zerotest.response import Response
from zerotest.response_matcher import ResponseMatcher


matcher = ResponseMatcher(ignore_all_headers=True)
verify_ssl = False


def test_post_get_audit_state():
    request = Request(scheme='http', method='POST', headers={'Connection': 'keep-alive', 'Content-Length': '0', 'Accept': '*/*', 'Origin': 'http://127.0.0.1:9000', 'X-Requested-With': 'XMLHttpRequest', 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.28 Safari/537.36', 'Dnt': '1', 'Content-Type': 'application/json', 'Referer': 'http://127.0.0.1:9000/', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US,en;q=0.9,eo;q=0.8', 'Cookie': 'gsScrollPos-6417=0; gsScrollPos-5300=0; gsScrollPos-2934=0; gsScrollPos-3120=0; gsScrollPos-3574=0; gsScrollPos-3508=; gsScrollPos-4736=0; gsScrollPos-3571=0; gsScrollPos-3123=0'}, host='127.0.0.1:5000', path='/get-audit-state')
    
    real = Response.from_requests_response(request.send_request(verify=verify_ssl))
    expect = Response(status=200, headers={'content-type': 'application/json'}, body='{"all_contests":null,"all_interpretations":[],"audit_name":null,"audit_type_name":null,"ballot_ids":null,"ballot_manifest":null,"cvr_hash":null,"main_contest_in_progress":null,"reported_results":null,"seed":null,"total_number_of_ballots":null}\n')
    matcher.match_responses(expect, real)


def test_get_get_audit_types():
    request = Request(scheme='http', method='GET', headers={'Connection': 'keep-alive', 'Accept': '*/*', 'Dnt': '1', 'X-Requested-With': 'XMLHttpRequest', 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.28 Safari/537.36', 'Content-Type': 'application/json', 'Referer': 'http://127.0.0.1:9000/', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US,en;q=0.9,eo;q=0.8', 'Cookie': 'gsScrollPos-6417=0; gsScrollPos-5300=0; gsScrollPos-2934=0; gsScrollPos-3120=0; gsScrollPos-3574=0; gsScrollPos-3508=; gsScrollPos-4736=0; gsScrollPos-3571=0; gsScrollPos-3123=0'}, host='127.0.0.1:5000', path='/get-audit-types')
    
    real = Response.from_requests_response(request.send_request(verify=verify_ssl))
    expect = Response(status=200, headers={'content-type': 'application/json'}, body='{"types":["ballot_polling","ballot_comparison"]}\n')
    matcher.match_responses(expect, real)


def test_post_set_audit_type():
    request = Request(scheme='http', method='POST', headers={'Connection': 'keep-alive', 'Content-Length': '28', 'Accept': '*/*', 'Origin': 'http://127.0.0.1:9000', 'X-Requested-With': 'XMLHttpRequest', 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.28 Safari/537.36', 'Dnt': '1', 'Content-Type': 'application/json', 'Referer': 'http://127.0.0.1:9000/', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US,en;q=0.9,eo;q=0.8', 'Cookie': 'gsScrollPos-6417=0; gsScrollPos-5300=0; gsScrollPos-2934=0; gsScrollPos-3120=0; gsScrollPos-3574=0; gsScrollPos-3508=; gsScrollPos-4736=0; gsScrollPos-3571=0; gsScrollPos-3123=0'}, host='127.0.0.1:5000', path='/set-audit-type', data='{"type":"ballot_comparison"}')
    
    real = Response.from_requests_response(request.send_request(verify=verify_ssl))
    expect = Response(status=200, headers={'content-type': 'text/html; charset=utf-8'}, body='')
    matcher.match_responses(expect, real)


def test_post_get_audit_state_1():
    request = Request(scheme='http', method='POST', headers={'Connection': 'keep-alive', 'Content-Length': '0', 'Accept': '*/*', 'Origin': 'http://127.0.0.1:9000', 'X-Requested-With': 'XMLHttpRequest', 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.28 Safari/537.36', 'Dnt': '1', 'Content-Type': 'application/json', 'Referer': 'http://127.0.0.1:9000/', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US,en;q=0.9,eo;q=0.8', 'Cookie': 'gsScrollPos-6417=0; gsScrollPos-5300=0; gsScrollPos-2934=0; gsScrollPos-3120=0; gsScrollPos-3574=0; gsScrollPos-3508=; gsScrollPos-4736=0; gsScrollPos-3571=0; gsScrollPos-3123=0'}, host='127.0.0.1:5000', path='/get-audit-state')
    
    real = Response.from_requests_response(request.send_request(verify=verify_ssl))
    expect = Response(status=200, headers={'content-type': 'application/json'}, body='{"all_contests":[{"candidates":["DEM Sheldon Whitehouse","REP Robert G. Flanders Jr."],"id":"senator","title":"Senator in Congress"},{"candidates":["DEM David N. Cicilline (13215)","REP Patrick J. Donovan"],"id":"rep_1","title":"Representative in Congress District 1 (13213)"},{"candidates":["DEM Gina M. Raimondo","MOD William H. Gilbert","REP Allan W. Fung","Com Anne Armstrong","Ind Luis Daniel Munoz","Ind Joseph A. Trillo"],"id":"governor","title":"Governor"},{"candidates":["DEM Daniel J. McKee","MOD Joel J. Hellmann","REP Paul E. Pence","Ind Jonathan J. Riccitelli","Ind Ross K. McCurdy"],"id":"lieutenant_governor","title":"Lieutenant Governor"},{"candidates":["DEM Nellie M. Gorbea","REP Pat V. Cortellessa"],"id":"secretary_of_state","title":"Secretary of State"},{"candidates":["DEM Peter F. Neronha","Com Alan Gordon"],"id":"attorney_general","title":"Attorney General"},{"candidates":["DEM Seth Magaziner","REP Michael G. Riley"],"id":"treasurer","title":"General Treasurer"},{"candidates":["Approve","Reject"],"id":"issue_1","title":"1. RHODE ISLAND SCHOOL BUILDINGS - $250,000,000"},{"candidates":["Approve","Reject"],"id":"issue_2","title":"2. HIGHER EDUCATION FACILITIES - $70,000,000"},{"candidates":["Approve","Reject"],"id":"issue_3","title":"3. GREEN ECONOMY AND CLEAN WATER - $47,300,000"}],"all_interpretations":[],"audit_name":null,"audit_type_name":"ballot_comparison","ballot_ids":null,"ballot_manifest":null,"cvr_hash":null,"main_contest_in_progress":null,"reported_results":[{"contest_id":"senator","results":[{"candidate":"DEM Sheldon Whitehouse","proportion":0.595,"votes":5367},{"candidate":"REP Robert G. Flanders Jr.","proportion":0.389,"votes":3506},{"candidate":"Write-in","proportion":0.002,"votes":19},{"candidate":"undervote","proportion":0.014,"votes":127},{"candidate":"overvote","proportion":0.0002,"votes":2}]},{"contest_id":"rep_1","results":[{"candidate":"DEM David N. Cicilline (13215)","proportion":0.601,"votes":5424},{"candidate":"REP Patrick J. Donovan","proportion":0.379,"votes":3417},{"candidate":"Write-in","proportion":0.001,"votes":13},{"candidate":"undervote","proportion":0.018,"votes":166},{"candidate":"overvote","proportion":0.0001,"votes":1}]},{"contest_id":"governor","results":[{"candidate":"DEM Gina M. Raimondo","proportion":0.526,"votes":4749},{"candidate":"MOD William H. Gilbert","proportion":0.028,"votes":256},{"candidate":"REP Allan W. Fung","proportion":0.343,"votes":3094},{"candidate":"Com Anne Armstrong","proportion":0.011,"votes":103},{"candidate":"Ind Luis Daniel Munoz","proportion":0.014,"votes":123},{"candidate":"Ind Joseph A. Trillo","proportion":0.056,"votes":509},{"candidate":"Write-in","proportion":0.004,"votes":32},{"candidate":"undervote","proportion":0.016,"votes":143},{"candidate":"overvote","proportion":0.001,"votes":12}]},{"contest_id":"lieutenant_governor","results":[{"candidate":"DEM Daniel J. McKee","proportion":0.575,"votes":5184},{"candidate":"MOD Joel J. Hellmann","proportion":0.032,"votes":291},{"candidate":"REP Paul E. Pence","proportion":0.273,"votes":2464},{"candidate":"Ind Jonathan J. Riccitelli","proportion":0.028,"votes":251},{"candidate":"Ind Ross K. McCurdy","proportion":0.022,"votes":202},{"candidate":"Write-in","proportion":0.015,"votes":137},{"candidate":"undervote","proportion":0.054,"votes":490},{"candidate":"overvote","proportion":0.0002,"votes":2}]},{"contest_id":"secretary_of_state","results":[{"candidate":"DEM Nellie M. Gorbea","proportion":0.651,"votes":5873},{"candidate":"REP Pat V. Cortellessa","proportion":0.306,"votes":2757},{"candidate":"Write-in","proportion":0.001,"votes":10},{"candidate":"undervote","proportion":0.042,"votes":381},{"candidate":"overvote","proportion":0.0,"votes":0}]},{"contest_id":"attorney_general","results":[{"candidate":"DEM Peter F. Neronha","proportion":0.727,"votes":6560},{"candidate":"Com Alan Gordon","proportion":0.163,"votes":1468},{"candidate":"Write-in","proportion":0.006,"votes":51},{"candidate":"undervote","proportion":0.104,"votes":941},{"candidate":"overvote","proportion":0.0001,"votes":1}]},{"contest_id":"treasurer","results":[{"candidate":"DEM Seth Magaziner","proportion":0.658,"votes":5932},{"candidate":"REP Michael G. Riley","proportion":0.305,"votes":2751},{"candidate":"Write-in","proportion":0.008,"votes":7},{"candidate":"undervote","proportion":0.037,"votes":330},{"candidate":"overvote","proportion":0.0001,"votes":1}]},{"contest_id":"issue_1","results":[{"candidate":"Approve","proportion":0.724,"votes":6534},{"candidate":"Reject","proportion":0.225,"votes":2027},{"candidate":"undervote","proportion":0.051,"votes":459},{"candidate":"overvote","proportion":0.0001,"votes":1}]},{"contest_id":"issue_2","results":[{"candidate":"Approve","proportion":0.53,"votes":4779},{"candidate":"Reject","proportion":0.411,"votes":3708},{"candidate":"undervote","proportion":0.059,"votes":533},{"candidate":"overvote","proportion":0.0001,"votes":1}]},{"contest_id":"issue_3","results":[{"candidate":"Approve","proportion":0.749,"votes":6753},{"candidate":"Reject","proportion":0.197,"votes":1779},{"candidate":"undervote","proportion":0.054,"votes":489}]}],"seed":null,"total_number_of_ballots":null}\n')
    matcher.match_responses(expect, real)


def test_post_set_audit_name():
    request = Request(scheme='http', method='POST', headers={'Connection': 'keep-alive', 'Content-Length': '38', 'Accept': '*/*', 'Origin': 'http://127.0.0.1:9000', 'X-Requested-With': 'XMLHttpRequest', 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.28 Safari/537.36', 'Dnt': '1', 'Content-Type': 'application/json', 'Referer': 'http://127.0.0.1:9000/', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US,en;q=0.9,eo;q=0.8', 'Cookie': 'gsScrollPos-6417=0; gsScrollPos-5300=0; gsScrollPos-2934=0; gsScrollPos-3120=0; gsScrollPos-3574=0; gsScrollPos-3508=; gsScrollPos-4736=0; gsScrollPos-3571=0; gsScrollPos-3123=0'}, host='127.0.0.1:5000', path='/set-audit-name', data='{"audit_name":"comparison-zerotest-2"}')
    
    real = Response.from_requests_response(request.send_request(verify=verify_ssl))
    expect = Response(status=200, headers={'content-type': 'text/html; charset=utf-8'}, body='')
    matcher.match_responses(expect, real)


def test_post_get_audit_state_2():
    request = Request(scheme='http', method='POST', headers={'Connection': 'keep-alive', 'Content-Length': '0', 'Accept': '*/*', 'Origin': 'http://127.0.0.1:9000', 'X-Requested-With': 'XMLHttpRequest', 'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.28 Safari/537.36', 'Dnt': '1', 'Content-Type': 'application/json', 'Referer': 'http://127.0.0.1:9000/', 'Accept-Encoding': 'gzip, deflate, br', 'Accept-Language': 'en-US,en;q=0.9,eo;q=0.8', 'Cookie': 'gsScrollPos-6417=0; gsScrollPos-5300=0; gsScrollPos-2934=0; gsScrollPos-3120=0; gsScrollPos-3574=0; gsScrollPos-3508=; gsScrollPos-4736=0; gsScrollPos-3571=0; gsScrollPos-3123=0'}, host='127.0.0.1:5000', path='/get-audit-state')
    
    real = Response.from_requests_response(request.send_request(verify=verify_ssl))
    expect = Response(status=200, headers={'content-type': 'application/json'}, body='{"all_contests":[{"candidates":["DEM Sheldon Whitehouse","REP Robert G. Flanders Jr."],"id":"senator","title":"Senator in Congress"},{"candidates":["DEM David N. Cicilline (13215)","REP Patrick J. Donovan"],"id":"rep_1","title":"Representative in Congress District 1 (13213)"},{"candidates":["DEM Gina M. Raimondo","MOD William H. Gilbert","REP Allan W. Fung","Com Anne Armstrong","Ind Luis Daniel Munoz","Ind Joseph A. Trillo"],"id":"governor","title":"Governor"},{"candidates":["DEM Daniel J. McKee","MOD Joel J. Hellmann","REP Paul E. Pence","Ind Jonathan J. Riccitelli","Ind Ross K. McCurdy"],"id":"lieutenant_governor","title":"Lieutenant Governor"},{"candidates":["DEM Nellie M. Gorbea","REP Pat V. Cortellessa"],"id":"secretary_of_state","title":"Secretary of State"},{"candidates":["DEM Peter F. Neronha","Com Alan Gordon"],"id":"attorney_general","title":"Attorney General"},{"candidates":["DEM Seth Magaziner","REP Michael G. Riley"],"id":"treasurer","title":"General Treasurer"},{"candidates":["Approve","Reject"],"id":"issue_1","title":"1. RHODE ISLAND SCHOOL BUILDINGS - $250,000,000"},{"candidates":["Approve","Reject"],"id":"issue_2","title":"2. HIGHER EDUCATION FACILITIES - $70,000,000"},{"candidates":["Approve","Reject"],"id":"issue_3","title":"3. GREEN ECONOMY AND CLEAN WATER - $47,300,000"}],"all_interpretations":[],"audit_name":"comparison-zerotest-2","audit_type_name":"ballot_comparison","ballot_ids":null,"ballot_manifest":null,"cvr_hash":null,"main_contest_in_progress":null,"reported_results":[{"contest_id":"senator","results":[{"candidate":"DEM Sheldon Whitehouse","proportion":0.595,"votes":5367},{"candidate":"REP Robert G. Flanders Jr.","proportion":0.389,"votes":3506},{"candidate":"Write-in","proportion":0.002,"votes":19},{"candidate":"undervote","proportion":0.014,"votes":127},{"candidate":"overvote","proportion":0.0002,"votes":2}]},{"contest_id":"rep_1","results":[{"candidate":"DEM David N. Cicilline (13215)","proportion":0.601,"votes":5424},{"candidate":"REP Patrick J. Donovan","proportion":0.379,"votes":3417},{"candidate":"Write-in","proportion":0.001,"votes":13},{"candidate":"undervote","proportion":0.018,"votes":166},{"candidate":"overvote","proportion":0.0001,"votes":1}]},{"contest_id":"governor","results":[{"candidate":"DEM Gina M. Raimondo","proportion":0.526,"votes":4749},{"candidate":"MOD William H. Gilbert","proportion":0.028,"votes":256},{"candidate":"REP Allan W. Fung","proportion":0.343,"votes":3094},{"candidate":"Com Anne Armstrong","proportion":0.011,"votes":103},{"candidate":"Ind Luis Daniel Munoz","proportion":0.014,"votes":123},{"candidate":"Ind Joseph A. Trillo","proportion":0.056,"votes":509},{"candidate":"Write-in","proportion":0.004,"votes":32},{"candidate":"undervote","proportion":0.016,"votes":143},{"candidate":"overvote","proportion":0.001,"votes":12}]},{"contest_id":"lieutenant_governor","results":[{"candidate":"DEM Daniel J. McKee","proportion":0.575,"votes":5184},{"candidate":"MOD Joel J. Hellmann","proportion":0.032,"votes":291},{"candidate":"REP Paul E. Pence","proportion":0.273,"votes":2464},{"candidate":"Ind Jonathan J. Riccitelli","proportion":0.028,"votes":251},{"candidate":"Ind Ross K. McCurdy","proportion":0.022,"votes":202},{"candidate":"Write-in","proportion":0.015,"votes":137},{"candidate":"undervote","proportion":0.054,"votes":490},{"candidate":"overvote","proportion":0.0002,"votes":2}]},{"contest_id":"secretary_of_state","results":[{"candidate":"DEM Nellie M. Gorbea","proportion":0.651,"votes":5873},{"candidate":"REP Pat V. Cortellessa","proportion":0.306,"votes":2757},{"candidate":"Write-in","proportion":0.001,"votes":10},{"candidate":"undervote","proportion":0.042,"votes":381},{"candidate":"overvote","proportion":0.0,"votes":0}]},{"contest_id":"attorney_general","results":[{"candidate":"DEM Peter F. Neronha","proportion":0.727,"votes":6560},{"candidate":"Com Alan Gordon","proportion":0.163,"votes":1468},{"candidate":"Write-in","proportion":0.006,"votes":51},{"candidate":"undervote","proportion":0.104,"votes":941},{"candidate":"overvote","proportion":0.0001,"votes":1}]},{"contest_id":"treasurer","results":[{"candidate":"DEM Seth Magaziner","proportion":0.658,"votes":5932},{"candidate":"REP Michael G. Riley","proportion":0.305,"votes":2751},{"candidate":"Write-in","proportion":0.008,"votes":7},{"candidate":"undervote","proportion":0.037,"votes":330},{"candidate":"overvote","proportion":0.0001,"votes":1}]},{"contest_id":"issue_1","results":[{"candidate":"Approve","proportion":0.724,"votes":6534},{"candidate":"Reject","proportion":0.225,"votes":2027},{"candidate":"undervote","proportion":0.051,"votes":459},{"candidate":"overvote","proportion":0.0001,"votes":1}]},{"contest_id":"issue_2","results":[{"candidate":"Approve","proportion":0.53,"votes":4779},{"candidate":"Reject","proportion":0.411,"votes":3708},{"candidate":"undervote","proportion":0.059,"votes":533},{"candidate":"overvote","proportion":0.0001,"votes":1}]},{"contest_id":"issue_3","results":[{"candidate":"Approve","proportion":0.749,"votes":6753},{"candidate":"Reject","proportion":0.197,"votes":1779},{"candidate":"undervote","proportion":0.054,"votes":489}]}],"seed":null,"total_number_of_ballots":null}\n')
    matcher.match_responses(expect, real)


