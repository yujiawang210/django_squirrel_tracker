TOOLS FOR ANALYTICS
SECTION 1
GROUP 5

Yujia Wang
Qiaochu Ren
UNIs: [yw3400, qr2128]

Description: This is the squirrel tracker website, which allows you to keep track of all the known squirrels. 

The squirrel tracker website has the following views:
1) A view that shows a map displaying the location of all squirrel sightings.(Location: /map)
2) A view that lists all squirrel sightings with links to create a sighting, edit a sighting, and see sighting stats. Please note that if the inputs cannot pass validation (i.e. duplicate unique squirrel id, missing required fields), the form will not let you update or create a sighting. (Location: /sightings)
   a) Create Sighting (Location: /sightings/add)
   b) Update Sighting (Location: /sighting/<unique-squirrel-id>)
   c) Sighting Stats (Location: /sighting/stats)

The squirrel tracker application also includes the following management commands:
1) An import command that is used to import data from a csv file. The file path should be specified at the command line after the name of the management command. (i.e. $ python manage.py import_squirrel_data /path/to/file.csv)
2) An export command that is used to export data in csv format. The file path should be specified at the command line after the name of the management command. (i.e. $ python manage.py export_squirrel_data /path/to/file.csv)

Deployment Link: 
https://my-project-ieor4501.appspot.com/sightings/

GitHub Link:
https://github.com/yujiawang210/squirreltracker.git

 
