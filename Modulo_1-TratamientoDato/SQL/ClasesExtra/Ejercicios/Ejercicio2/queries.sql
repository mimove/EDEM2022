
-- SELECT pilot_id, race_id, lap_number, min(lap_time) FROM lap group by pilot_id, race_id, lap_number;

-- create table Fastest_Laps as (SELECT id_lap, pilot_id, race_id, lap_number, min(lap_time) FROM lap group by id_lap, pilot_id, race_id, lap_number);


select count(*) from (SELECT pilot_id, race_id, lap_number, min(lap_time) FROM lap group by pilot_id, race_id, lap_number) as count1;

select count(*) from (SELECT id_lap, pilot_id, race_id, lap_number, min(lap_time) FROM lap group by id_lap, pilot_id, race_id, lap_number) as count2;


select count(*) from lap where NOT EXISTS (SELECT * from Fastest_Laps where lap.pilot_id = Fastest_Laps.pilot_id AND lap.race_id = Fastest_Laps.race_id AND lap.l) as count3;