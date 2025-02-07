WITH DailyAverages AS (
    SELECT 
        "DayofYear", 
        AVG("Temp_C") AS AvgTempByDay, 
        AVG("Temp_F") AS AvgTempByDay_F, 
        AVG("Humidity") AS AvgHumidity,
        AVG("WindSpeed(Km/h)") AS AvgWindSpeed
    FROM 
        public."Weather" 
    GROUP BY 
        "DayofYear"
)
SELECT 
    w.*, 
    da.AvgTempByDay,
    da.AvgTempByDay_F, 
    da.AvgHumidity,
    da.AvgWindSpeed
FROM 
    public."Weather" w
JOIN 
    DailyAverages da ON w."DayofYear" = da."DayofYear"
ORDER BY 
    w."DayofYear";
	