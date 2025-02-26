import sys
import os

def extract_logs(target_date, log_file="logs_2024.log", output_dir="output"):
    # Ensure output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_file = os.path.join(output_dir, f"output_{target_date}.txt")

    try:
        with open(log_file, "r", encoding="utf-8") as file, open(output_file, "w", encoding="utf-8") as out_file:
            for line in file:
                if line.startswith(target_date):  # Efficient filtering
                    out_file.write(line)
        
        print(f"Logs for {target_date} extracted to {output_file}")

    except FileNotFoundError:
        print(f"Error: Log file '{log_file}' not found.")
    except Exception as e:
        print(f"Error processing file: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python extract_logs.py <YYYY-MM-DD>")
        sys.exit(1)

    date_to_extract = sys.argv[1]
    extract_logs(date_to_extract)