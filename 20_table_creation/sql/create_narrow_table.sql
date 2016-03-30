-- Copyright 2015 Silicon Valley Data Science.
--
-- Licensed under the Apache License, Version 2.0 (the "License");
-- you may not use this file except in compliance with the License.
-- You may obtain a copy of the License at
--
--      http://www.apache.org/licenses/LICENSE-2.0
--
-- Unless required by applicable law or agreed to in writing, software
-- distributed under the License is distributed on an "AS IS" BASIS,
-- WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
-- See the License for the specific language governing permissions and
-- limitations under the License.

USE strataca2016;

DROP TABLE IF EXISTS narrow;

CREATE TABLE narrow (
  ip string,
  user_name string,
  unix_time bigint,
  time string,
  url string,
  domain string,
  page string,
  port smallint,
  referer string,
  agent string
)
ROW FORMAT DELIMITED FIELDS TERMINATED BY "|"
LINES TERMINATED BY '\n'
STORED as TEXTFILE;

-- Load data 
LOAD DATA inpath '${hivevar:datapath}' into table narrow;

