import sys
from typing import NewType, List, Dict, Set
from collections import defaultdict, deque

SatelliteId = NewType("SatelliteId", int)

def on_satellite_reported_back(satellite_id: SatelliteId) -> None:
    print(f"SatelliteReportedBack: {satellite_id}")

def err_duplicate_satellite(satellite_id: SatelliteId) -> None:
    print(f"E1: {satellite_id}")

def err_invalid_satellite(satellite_id: SatelliteId) -> None:
    print(f"E2: {satellite_id}")

class SatelliteNetwork:
    def _init_(self):
        self.connected = set()
        self.relationships = defaultdict(set)
    
    def satellite_connected(self, satellite_id: SatelliteId) -> None:
        if satellite_id in self.connected:
            err_duplicate_satellite(satellite_id)
        else:
            self.connected.add(satellite_id)
    
    def relationship_established(self, satellite_id1: SatelliteId, satellite_id2: SatelliteId) -> None:
        if satellite_id1 not in self.connected or satellite_id2 not in self.connected:
            if satellite_id1 not in self.connected:
                err_invalid_satellite(satellite_id1)
            if satellite_id2 not in self.connected:
                err_invalid_satellite(satellite_id2)
            return
        
        self.relationships[satellite_id1].add(satellite_id2)
        self.relationships[satellite_id2].add(satellite_id1)
    
    def message_received(self, satellite_ids: List[SatelliteId]) -> None:
        # Validate all satellites exist
        for sat_id in satellite_ids:
            if sat_id not in self.connected:
                err_invalid_satellite(sat_id)
                return
        
        # BFS setup
        received_time = {}
        queue = deque()
        reports = []
        
        # Initialize with first notified satellites
        for sat_id in satellite_ids:
            received_time[sat_id] = 0
            queue.append((sat_id, 0))
        
        # Process notifications
        while queue:
            current_sat, current_time = queue.popleft()
            
            # Schedule report (current_time + 30)
            reports.append((current_time + 30, current_sat))
            
            # Notify neighbors in order
            for neighbor in sorted(self.relationships[current_sat]):
                if neighbor not in received_time:
                    received_time[neighbor] = current_time + 10
                    queue.append((neighbor, current_time + 10))
        
        # Output reports in order
        for time, sat_id in sorted(reports):
            on_satellite_reported_back(sat_id)

def main():
    network = SatelliteNetwork()
    no_commands = int(sys.stdin.readline())
    
    for _ in range(no_commands):
        line = sys.stdin.readline().strip()
        if not line:
            continue
            
        parts = line.split()
        cmd = parts[0]
        args = list(map(int, parts[1:]))
        
        if cmd == "SatelliteConnected":
            network.satellite_connected(SatelliteId(args[0]))
        elif cmd == "RelationshipEstablished":
            network.relationship_established(SatelliteId(args[0]), SatelliteId(args[1]))
        elif cmd == "MessageReceived":
            m = args[0]
            network.message_received([SatelliteId(sid) for sid in args[1:m+1]])

if _name_ == "_main_":
    main() 