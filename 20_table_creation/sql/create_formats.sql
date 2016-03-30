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
  
-- ORC
drop table if exists ${hivevar:table}_orc;
create table ${hivevar:table}_orc stored as orc tblproperties ("orc.compress"="SNAPPY") as select * from ${hivevar:table};
 
-- Parquet
set parquet.compression=SNAPPY;
drop table if exists ${hivevar:table}_parquet;
create table ${hivevar:table}_parquet stored as parquet as select * from ${hivevar:table};

-- Sequence File 
set hive.exec.compress.output=true;
set mapreduce.output.fileoutputformat.compress.type=BLOCK;
set mapreduce.output.fileoutputformat.compress.codec=org.apache.hadoop.io.compress.SnappyCodec;
drop table if exists ${hivevar:table}_sequencefile;
create table ${hivevar:table}_sequencefile stored as sequencefile as select * from ${hivevar:table};
 
-- Avro (deflate)
set hive.exec.compress.output=true;
set avro.output.codec=deflate;
drop table if exists ${hivevar:table}_avro_deflate;
create table ${hivevar:table}_avro_deflate
	row format serde 'org.apache.hadoop.hive.serde2.avro.AvroSerDe'
	stored as inputformat 'org.apache.hadoop.hive.ql.io.avro.AvroContainerInputFormat'
	outputformat 'org.apache.hadoop.hive.ql.io.avro.AvroContainerOutputFormat'
	tblproperties ('avro.schema.url'= '${hivevar:avroschema}');
insert into table ${hivevar:table}_avro_deflate select * from ${hivevar:table};

-- Avro (snappy)
set hive.exec.compress.output=true;
set avro.output.codec=snappy;
drop table if exists ${hivevar:table}_avro_snappy;
create table ${hivevar:table}_avro_snappy
        row format serde 'org.apache.hadoop.hive.serde2.avro.AvroSerDe'
        stored as inputformat 'org.apache.hadoop.hive.ql.io.avro.AvroContainerInputFormat'
        outputformat 'org.apache.hadoop.hive.ql.io.avro.AvroContainerOutputFormat'
        tblproperties ('avro.schema.url'= '${hivevar:avroschema}');
insert into table ${hivevar:table}_avro_snappy select * from ${hivevar:table};
 
-- Text
set hive.exec.compress.output=true;
set mapreduce.output.fileoutputformat.compress.codec=org.apache.hadoop.io.compress.SnappyCodec;
drop table if exists ${hivevar:table}_text;
create table ${hivevar:table}_text stored as textfile as select * from ${hivevar:table};

