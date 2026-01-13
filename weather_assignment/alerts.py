def generate_alerts(readings):
    alerts = {}
    rain_total = {}

    for r in readings:
        #print(r)
        date = str(r.timestamp.date())
        station = r.station_id

        if station not in alerts:
            alerts[station] = {}
        if date not in alerts[station]:
            alerts[station][date] = []
        if station not in rain_total:
            rain_total[station] = {}
        if date not in rain_total[station]:
            rain_total[station][date] = 0

        if r.temperature > 40:
            if "HEAT_ALERT" not in alerts[station][date]:
                alerts[station][date].append("HEAT_ALERT")

        rain_total[station][date] += r.rainfall

    for station in rain_total:
        for date in rain_total[station]:
            if rain_total[station][date] > 100:
                if "HEAVY_RAIN_ALERT" not in alerts[station][date]:
                    alerts[station][date].append("HEAVY_RAIN_ALERT")

    return alerts
