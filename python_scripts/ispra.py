#!/usr/bin/env python3
"""
Script unificato per elaborare i dati ISPRA da file CSV.
Ciascun processo per C6H6, CO, NO2, O3, PM10, PM2.5 e SO2 viene eseguito separatamente.
L'output finale è un JSON aggregato che contiene le informazioni di ciascun inquinante.
"""

import csv
import sys
import json
import logging
from datetime import datetime

# Configurazione logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# -------------------------------------------------------------------
# PROCESSO PER C6H6
# -------------------------------------------------------------------
def process_c6h6():
    try:
        station_code = sys.argv[1] if len(sys.argv) > 1 else 'IT1658A'
        csv_file = sys.argv[2] if len(sys.argv) > 2 else '/config/dati_ispra/c6h6_data.csv'
        logger.info(f"[C6H6] Processing station: {station_code}")
        
        with open(csv_file, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            logger.debug(f"[C6H6] CSV headers: {reader.fieldnames}")
            records = []
            for row in reader:
                try:
                    if row.get('station_eu_code') == station_code:
                        records.append({
                            'time': row['data_record_end_time'],
                            'value': float(row['data_record_value']),
                            'row': row
                        })
                except (KeyError, ValueError) as e:
                    logger.warning(f"[C6H6] Error processing row: {e}")
                    continue

            if not records:
                logger.error(f"[C6H6] No data found for station {station_code}")
                return {"value": None, "error": "No data found"}

            records.sort(key=lambda x: x['time'], reverse=True)
            output = {
                "value": records[0]['value'],
                "station": records[0]['row']['station_name'],
                "last_measurement": records[0]['row']['data_record_end_time'],
                "latitude": records[0]['row']['station_lat'],
                "longitude": records[0]['row']['station_lon'],
                "full_data": records[0]['row']
            }
            return output

    except Exception as e:
        logger.error(f"[C6H6] Critical error: {str(e)}")
        return {"value": None, "error": str(e)}

# -------------------------------------------------------------------
# PROCESSO PER CO
# -------------------------------------------------------------------
def process_co():
    try:
        station_code = sys.argv[1] if len(sys.argv) > 1 else 'IT1658A'
        csv_file = sys.argv[2] if len(sys.argv) > 2 else '/config/dati_ispra/co_data.csv'
        logger.info(f"[CO] Processing station: {station_code}")
        
        with open(csv_file, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            logger.debug(f"[CO] CSV headers: {reader.fieldnames}")
            records = []
            for row in reader:
                try:
                    if row.get('station_eu_code') == station_code:
                        records.append({
                            'time': row['data_record_end_time'],
                            'value': float(row['data_record_value']),
                            'row': row
                        })
                except (KeyError, ValueError) as e:
                    logger.warning(f"[CO] Error processing row: {e}")
                    continue

            if not records:
                logger.error(f"[CO] No data found for station {station_code}")
                return {"value": None, "error": "No data found"}

            records.sort(key=lambda x: x['time'], reverse=True)
            output = {
                "value": records[0]['value'],
                "station": records[0]['row']['station_name'],
                "last_measurement": records[0]['row']['data_record_end_time'],
                "latitude": records[0]['row']['station_lat'],
                "longitude": records[0]['row']['station_lon'],
                "full_data": records[0]['row']
            }
            return output

    except Exception as e:
        logger.error(f"[CO] Critical error: {str(e)}")
        return {"value": None, "error": str(e)}

# -------------------------------------------------------------------
# PROCESSO PER NO2
# -------------------------------------------------------------------
def process_no2():
    try:
        station_code = sys.argv[1] if len(sys.argv) > 1 else 'IT1658A'
        # Attenzione: il file CSV di default è lo stesso del CO, come nello script originale.
        csv_file = sys.argv[2] if len(sys.argv) > 2 else '/config/dati_ispra/co_data.csv'
        logger.info(f"[NO2] Processing station: {station_code}")

        with open(csv_file, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            logger.debug(f"[NO2] CSV headers: {reader.fieldnames}")
            records = []
            for row in reader:
                try:
                    if row.get('station_eu_code') == station_code:
                        records.append({
                            'time': row['data_record_end_time'],
                            'value': float(row['data_record_value']),
                            'row': row
                        })
                except (KeyError, ValueError) as e:
                    logger.warning(f"[NO2] Error processing row: {e}")
                    continue

            if not records:
                logger.error(f"[NO2] No data found for station {station_code}")
                return {"value": None, "error": "No data found"}

            records.sort(key=lambda x: x['time'], reverse=True)
            output = {
                "value": records[0]['value'],
                "station": records[0]['row']['station_name'],
                "last_measurement": records[0]['row']['data_record_end_time'],
                "latitude": records[0]['row']['station_lat'],
                "longitude": records[0]['row']['station_lon'],
                "full_data": records[0]['row']
            }
            return output

    except Exception as e:
        logger.error(f"[NO2] Critical error: {str(e)}")
        return {"value": None, "error": str(e)}

# -------------------------------------------------------------------
# PROCESSO PER O3
# -------------------------------------------------------------------
def process_o3():
    try:
        station_code = sys.argv[1] if len(sys.argv) > 1 else 'IT2139A'
        csv_file = sys.argv[2] if len(sys.argv) > 2 else '/config/dati_ispra/o3_data.csv'
        logger.info(f"[O3] Processing station: {station_code}")

        with open(csv_file, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            logger.debug(f"[O3] CSV headers: {reader.fieldnames}")
            records = []
            for row in reader:
                try:
                    if row.get('station_eu_code') == station_code:
                        records.append({
                            'time': row['data_record_end_time'],
                            'value': float(row['data_record_value']),
                            'row': row
                        })
                except (KeyError, ValueError) as e:
                    logger.warning(f"[O3] Error processing row: {e}")
                    continue

            if not records:
                logger.error(f"[O3] No data found for station {station_code}")
                return {"value": None, "error": "No data found"}

            records.sort(key=lambda x: x['time'], reverse=True)
            output = {
                "value": records[0]['value'],
                "station": records[0]['row']['station_name'],
                "last_measurement": records[0]['row']['data_record_end_time'],
                "latitude": records[0]['row']['station_lat'],
                "longitude": records[0]['row']['station_lon'],
                "full_data": records[0]['row']
            }
            return output

    except Exception as e:
        logger.error(f"[O3] Critical error: {str(e)}")
        return {"value": None, "error": str(e)}

# -------------------------------------------------------------------
# PROCESSO PER PM10
# -------------------------------------------------------------------
def process_pm10():
    try:
        station_code = sys.argv[1] if len(sys.argv) > 1 else 'IT1658A'
        csv_file = sys.argv[2] if len(sys.argv) > 2 else '/config/dati_ispra/pm10_data.csv'
        logger.info(f"[PM10] Processing station: {station_code}")

        with open(csv_file, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            logger.debug(f"[PM10] CSV headers: {reader.fieldnames}")
            records = []
            for row in reader:
                try:
                    if row.get('station_eu_code') == station_code:
                        records.append({
                            'time': row['data_record_end_time'],
                            'value': float(row['data_record_value']),
                            'row': row
                        })
                except (KeyError, ValueError) as e:
                    logger.warning(f"[PM10] Error processing row: {e}")
                    continue

            if not records:
                logger.error(f"[PM10] No data found for station {station_code}")
                return {"value": None, "error": "No data found"}

            records.sort(key=lambda x: x['time'], reverse=True)
            output = {
                "value": records[0]['value'],
                "station": records[0]['row']['station_name'],
                "last_measurement": records[0]['row']['data_record_end_time'],
                "latitude": records[0]['row']['station_lat'],
                "longitude": records[0]['row']['station_lon'],
                "full_data": records[0]['row']
            }
            return output

    except Exception as e:
        logger.error(f"[PM10] Critical error: {str(e)}")
        return {"value": None, "error": str(e)}

# -------------------------------------------------------------------
# PROCESSO PER PM2.5
# -------------------------------------------------------------------
def process_pm25():
    try:
        station_code = sys.argv[1] if len(sys.argv) > 1 else 'IT1658A'
        csv_file = sys.argv[2] if len(sys.argv) > 2 else '/config/dati_ispra/pm25_data.csv'
        logger.info(f"[PM2.5] Processing station: {station_code}")

        with open(csv_file, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            logger.debug(f"[PM2.5] CSV headers: {reader.fieldnames}")
            records = []
            for row in reader:
                try:
                    if row.get('station_eu_code') == station_code:
                        records.append({
                            'time': row['data_record_end_time'],
                            'value': float(row['data_record_value']),
                            'row': row
                        })
                except (KeyError, ValueError) as e:
                    logger.warning(f"[PM2.5] Error processing row: {e}")
                    continue

            if not records:
                logger.error(f"[PM2.5] No data found for station {station_code}")
                return {"value": None, "error": "No data found"}

            records.sort(key=lambda x: x['time'], reverse=True)
            output = {
                "value": records[0]['value'],
                "station": records[0]['row']['station_name'],
                "last_measurement": records[0]['row']['data_record_end_time'],
                "latitude": records[0]['row']['station_lat'],
                "longitude": records[0]['row']['station_lon'],
                "full_data": records[0]['row']
            }
            return output

    except Exception as e:
        logger.error(f"[PM2.5] Critical error: {str(e)}")
        return {"value": None, "error": str(e)}

# -------------------------------------------------------------------
# PROCESSO PER SO2
# -------------------------------------------------------------------
def process_so2():
    try:
        station_code = sys.argv[1] if len(sys.argv) > 1 else 'IT1658A'
        csv_file = sys.argv[2] if len(sys.argv) > 2 else '/config/dati_ispra/so2_data.csv'
        logger.info(f"[SO2] Processing station: {station_code}")

        with open(csv_file, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            logger.debug(f"[SO2] CSV headers: {reader.fieldnames}")
            records = []
            for row in reader:
                try:
                    if row.get('station_eu_code') == station_code:
                        records.append({
                            'time': row['data_record_end_time'],
                            'value': float(row['data_record_value']),
                            'row': row
                        })
                except (KeyError, ValueError) as e:
                    logger.warning(f"[SO2] Error processing row: {e}")
                    continue

            if not records:
                logger.error(f"[SO2] No data found for station {station_code}")
                return {"value": None, "error": "No data found"}

            records.sort(key=lambda x: x['time'], reverse=True)
            output = {
                "value": records[0]['value'],
                "station": records[0]['row']['station_name'],
                "last_measurement": records[0]['row']['data_record_end_time'],
                "latitude": records[0]['row']['station_lat'],
                "longitude": records[0]['row']['station_lon'],
                "full_data": records[0]['row']
            }
            return output

    except Exception as e:
        logger.error(f"[SO2] Critical error: {str(e)}")
        return {"value": None, "error": str(e)}

# -------------------------------------------------------------------
# MAIN: aggrega i risultati di tutti i processi
# -------------------------------------------------------------------
def main():
    results = {
        "C6H6": process_c6h6(),
        "CO": process_co(),
        "NO2": process_no2(),
        "O3": process_o3(),
        "PM10": process_pm10(),
        "PM25": process_pm25(),
        "SO2": process_so2()
    }
    print(json.dumps(results))

if __name__ == '__main__':
    main()
