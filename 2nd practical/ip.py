# Initial configuration
server_ip = ("192", "168", "1", "100")  # Immutable tuple
allowed_ips = ["192.168.1.1", "192.168.1.10"]  # Mutable list

# Function to update allowed_ips
def update_allowed_ips(ip_list, new_ip):
    if new_ip not in ip_list:
        ip_list.append(new_ip)
        print(f"Added '{new_ip}' to allowed IPs.")
    else:
        print(f"'{new_ip}' is already allowed.")

# Function to display configuration
def display_config(server_ip, allowed_ips):
    print("\n--- Server Configuration ---")
    print(f"Server IP (immutable): {server_ip}")
    print(f"Allowed IPs (mutable): {allowed_ips}")

# ----- Usage -----
display_config(server_ip, allowed_ips)

# Update allowed IPs
update_allowed_ips(allowed_ips, "192.168.1.15")
update_allowed_ips(allowed_ips, "192.168.1.1")  # Already present

display_config(server_ip, allowed_ips)
