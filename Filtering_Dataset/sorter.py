import re
import tkinter as tk
from tkinter import filedialog, scrolledtext
import traceback

def reorder_genome_file(input_file, output_file, snp_list_file, log_output):
    try:
        autosomes = [[] for _ in range(22)]
        x_chromosome_data = []
        y_chromosome_data = []
        mt_dna_data = []

        with open(snp_list_file, 'r') as snp_file:
            snp_list = set(snp_file.read().strip().splitlines())
            total_snps_in_list = len(snp_list)

        seen_snps = set()

        with open(input_file, 'r') as file:
            header = file.readline().strip()
            output_data = [header]

            for line in file:
                line = line.strip()
                if not line:
                    continue

                normalized_line = re.sub(r'[ \t,]+', '\t', line)
                parts = normalized_line.split('\t')

                if len(parts) < 2:
                    continue

                snp_id = parts[0]
                chrom = parts[1]

                if snp_id not in snp_list or snp_id in seen_snps:
                    continue

                seen_snps.add(snp_id)

                if chrom.upper() == 'X':
                    x_chromosome_data.append(normalized_line)
                elif chrom.upper() == 'Y':
                    y_chromosome_data.append(normalized_line)
                elif chrom.upper() == 'MT':
                    mt_dna_data.append(normalized_line)
                elif chrom.isdigit():
                    chrom_index = int(chrom) - 1
                    if 0 <= chrom_index < 22:
                        autosomes[chrom_index].append(normalized_line)

            for i in range(22):
                output_data.extend(autosomes[i])
            output_data.extend(x_chromosome_data)
            output_data.extend(y_chromosome_data)
            output_data.extend(mt_dna_data)

        with open(output_file, 'w') as file:
            for line in output_data:
                file.write(line + '\n')

        total_lines_written = len(output_data)
        retained_snps = total_lines_written - 1
        coverage = (retained_snps / total_snps_in_list) * 100 if total_snps_in_list else 0

        log_output.insert(tk.END, "✅ File processing completed successfully.\n")
        log_output.insert(tk.END, f"📄 Total data rows (excluding header)(1240k coverage): {retained_snps}\n")
        log_output.insert(tk.END, f"📑 SNPs in list: {total_snps_in_list}\n")
        log_output.insert(tk.END, f"📊 Coverage: {coverage:.2f}% of SNP list matched\n\n")

    except Exception as e:
        log_output.insert(tk.END, f"❌ Error: {str(e)}\n")

def browse_file(entry):
    filepath = filedialog.askopenfilename()
    if filepath:
        entry.delete(0, tk.END)
        entry.insert(0, filepath)

def start_processing(input_entry, output_entry, snp_entry, log_output):
    try:
        input_file = input_entry.get()
        output_file = output_entry.get()
        snp_file = snp_entry.get()
        log_output.insert(tk.END, f"🔄 Processing...\n")
        reorder_genome_file(input_file, output_file, snp_file, log_output)
    except Exception as e:
        log_output.insert(tk.END, f"❌ Runtime Error: {traceback.format_exc()}\n")

# GUI Setup
root = tk.Tk()
root.title("Genome File Reorder Tool")

tk.Label(root, text="Input File:").grid(row=0, column=0, sticky="e")
input_entry = tk.Entry(root, width=50)
input_entry.grid(row=0, column=1)
tk.Button(root, text="Browse", command=lambda: browse_file(input_entry)).grid(row=0, column=2)

tk.Label(root, text="Output File:").grid(row=1, column=0, sticky="e")
output_entry = tk.Entry(root, width=50)
output_entry.grid(row=1, column=1)
tk.Button(root, text="Browse", command=lambda: browse_file(output_entry)).grid(row=1, column=2)

tk.Label(root, text="SNP List File:").grid(row=2, column=0, sticky="e")
snp_entry = tk.Entry(root, width=50)
snp_entry.grid(row=2, column=1)
tk.Button(root, text="Browse", command=lambda: browse_file(snp_entry)).grid(row=2, column=2)

log_output = scrolledtext.ScrolledText(root, width=70, height=15)
log_output.grid(row=4, column=0, columnspan=3, pady=10)

tk.Button(
    root, text="Start Processing",
    command=lambda: start_processing(input_entry, output_entry, snp_entry, log_output),
    bg='green', fg='white'
).grid(row=3, column=1, pady=10)

# Catch GUI crashes
try:
    root.mainloop()
except Exception as e:
    print("❌ GUI crashed:\n", traceback.format_exc())
