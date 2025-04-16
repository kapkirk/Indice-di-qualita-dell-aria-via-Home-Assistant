#!/usr/bin/env python3
"""
Script per leggere dati O3 da file CSV ISPRA
"""

import csv
import sys
import json
from datetime import datetime
import logging

# Configurazione logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    try:
        # Parametri in input
        station_code = sys.argv[1] if len(sys.argv) > 1 else 'IT2139A'
        csv_file = sys.argv[2] if len(sys.argv) > 2 else '/config/dati_ispra/03_data.csv'
        
        logger.info(f"Processing station: {station_code}")
        
        with open(csv_file, mode='r', encoding='utf-8') as f:
            # Leggi il file CSV con il delimiter corretto
            reader = csv.DictReader(f)
            
            logger.debug(f"CSV headers: {reader.fieldnames}")
            
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
                    logger.warning(f"Error processing row: {e}")
                    continue

            if not records:
                logger.error(f"No data found for station {station_code}")
                print(json.dumps({"value": None, "error": "No data found"}))
                return

            # Ordina per data (più recente prima)
            records.sort(key=lambda x: x['time'], reverse=True)
            
            # Prepara output per Home Assistant
            output = {
                "value": records[0]['value'],
                "station": records[0]['row']['station_name'],
                "last_measurement": records[0]['row']['data_record_end_time'],
                "latitude": records[0]['row']['station_lat'],
                "longitude": records[0]['row']['station_lon'],
                "full_data": records[0]['row']
            }
            
            print(json.dumps(output))

    except Exception as e:
        logger.error(f"Critical error: {str(e)}")
        print(json.dumps({"value": None, "error": str(e)}))

if __name__ == '__main__':
    main()