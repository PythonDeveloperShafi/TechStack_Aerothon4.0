# aerothon4.0
Finale project for Aerothon 4.0

# Backend configration for the main webpage.

-> The backend of the main webpage has been developed using Fast-API framework with postgresql for database.
-> There is only one end point "/files" which is used to download the required file (i.e. frontend 
    and backend templates) for the user in a single zip file.
-> The env_example file is provided to include access_key to the s3 bucket.
-> The end point "/files" requires two request parameters i.e. feTitle and beTitle representing title for
    frontend and backend.
