class CloudServiceProvider:
    def _init_(self, name, cpu_cost, memory_cost, storage_cost):
        self.name = name
        self.cpu_cost = cpu_cost  # Cost per CPU per hour
        self.memory_cost = memory_cost  # Cost per GB of RAM per hour
        self.storage_cost = storage_cost  # Cost per GB of storage per month

    def calculate_cost(self, cpus, memory, storage, hours=1):
        """ Calculate cost for the given resource usage """
        return (self.cpu_cost * cpus * hours) + (self.memory_cost * memory * hours) + (self.storage_cost * storage)
 def _str_(self):
        return f"{self.name}: CPU Cost: ${self.cpu_cost}/hour, Memory Cost: ${self.memory_cost}/GB/hour, Storage Cost: ${self.storage_cost}/GB/month"

class CloudCostEstimator:
    def _init_(self):
        self.providers = []
 # CRUD Operations
    def add_provider(self, provider):
        self.providers.append(provider)
        print(f"{provider.name} has been added.")
    def update_provider(self, provider_name, new_cpu_cost, new_memory_cost, new_storage_cost):
       for provider in self.providers:
            if provider.name == provider_name:
                provider.cpu_cost = new_cpu_cost
                provider.memory_cost = new_memory_cost
                provider.storage_cost = new_storage_cost
                print(f"{provider.name} has been updated.")
                return
        print(f"Provider {provider_name} not found.")

    def delete_provider(self, provider_name):
        for provider in self.providers:
            if provider.name == provider_name:
                self.providers.remove(provider)
                print(f"{provider_name} has been removed.")
                return
        print(f"Provider {provider_name} not found.")

    def list_providers(self):
        if not self.providers:
            print("No providers available.")
       for provider in self.providers:
            print(provider)
 # Cost Comparison
    def compare_costs(self, cpus, memory, storage, hours):
        print(f"\nComparing costs for {cpus} CPUs, {memory}GB Memory, {storage}GB Storage for {hours} hours:\n")
        for provider in self.providers:
            cost = provider.calculate_cost(cpus, memory, storage, hours)
            print(f"{provider.name}: Total Cost = ${cost:.2f}")
# Function to get user input for provider details
def get_provider_input():
    name = input("Enter the cloud provider name: ")
    cpu_cost = float(input(f"Enter the CPU cost per hour for {name}: "))
    memory_cost = float(input(f"Enter the memory cost per GB per hour for {name}: "))
    storage_cost = float(input(f"Enter the storage cost per GB per month for {name}: "))     
   
    return CloudServiceProvider(name, cpu_cost, memory_cost, storage_cost)
# Main function for user interaction
def main():
    estimator = CloudCostEstimator()
    while True:
        print("\n--- Cloud Cost Estimator ---")
        print("1. Add Cloud Provider")
        print("2. Update Cloud Provider")
        print("3. Delete Cloud Provider")
        print("4. List Cloud Providers")
        print("5. Compare Costs")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            provider = get_provider_input()
            estimator.add_provider(provider)

        elif choice == "2":
            name = input("Enter the cloud provider name to update: ")
            cpu_cost = float(input(f"Enter the new CPU cost per hour for {name}: "))
            memory_cost = float(input(f"Enter the new memory cost per GB per hour for {name}: "))
            storage_cost = float(input(f"Enter the new storage cost per GB per month for {name}: "))
            estimator.update_provider(name, cpu_cost, memory_cost, storage_cost)

        elif choice == "3":
            name = input("Enter the cloud provider name to delete: ")
            estimator.delete_provider(name)

        elif choice == "4":
            estimator.list_providers()

        elif choice == "5":
            cpus = int(input("Enter the number of CPUs: "))
            memory = float(input("Enter the amount of memory (in GB): "))
            storage = float(input("Enter the amount of storage (in GB): "))
            hours = int(input("Enter the number of hours: "))
            estimator.compare_costs(cpus, memory, storage, hours)

        elif choice == "6":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")
if _name_ == "_main_":
    main()
