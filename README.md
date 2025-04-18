

 ## NOVA RIDE BACKEND 

Nova rides is a Nova Scotia based application that intends to help rural community with low access to global ride sharing applications 
with the help of community persons.

#### BASE ASSUMPTION : 

1. User - within the local community or requests in a community
2. Provider - (While signup - provided where primarily served, Provider cannot serve more than 3 locations )

```mermaid
flowchart LR
    User --> Requests_Ride
    
    Requests_Ride --> Notifying_Service
    
    Notifying_Service --> |Push_Notification| Provider_1
    
    Notifying_Service --> |Push_Notification| Provider_2
    
    Notifying_Service --> |Push_Notification| Provider_3
    
    Provider_3 --> |Accepts_Ride| Request_User{User_Acceptance}
    
    Request_User --> |USER ACCEPTED| New_Ride
    
    Request_User --> |NOT ACCEPTED| Wait_For_Rides
    
    New_Ride --> END
    
    Wait_For_Rides --> END
```

