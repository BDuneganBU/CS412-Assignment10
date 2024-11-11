from socketserver import StreamRequestHandler
from django.db import models

# voter_analytics/models.py

class Voter(models.Model):
    '''The Voter model for each voter'''
    last_name = models.TextField()
    first_name = models.TextField()

    street_num = models.TextField()
    street_name = models.TextField()
    appartment_num = models.TextField()
    zip = models.TextField()

    dob = models.TextField()
    dor = models.TextField()
    affiliation = models.TextField()
    precinct = models.TextField()

    v20state = models.TextField()
    v21town = models.TextField()
    v21primary = models.TextField()
    v22general = models.TextField()
    v23town = models.TextField()
    voter_score = models.TextField()

    def __str__(self):
        '''Return a string representation of this model instance.'''
        return f'{self.first_name} {self.last_name} ({self.dob})'
    
def load_data():
        '''Function to load data records from CSV file into Django model instances.'''
        # delete existing records to prevent duplicates:
        Voter.objects.all().delete()
        
        filename = 'C:/Users/gowoo/Downloads/newton_voters.csv'
        f = open(filename)
        f.readline() # discard headers
        for line in f:
            fields = [field.strip().replace("\r", "").replace("\n", "") for field in line.split(',')]
            try:
                # create a new instance of Result object with this record from CSV
                result = Voter(
                        last_name = fields[1],
                        first_name = fields[2],

                        street_num = fields[3],
                        street_name = fields[4],
                        appartment_num = fields[5],
                        zip = fields[6],

                        dob = fields[7],
                        dor = fields[8],
                        affiliation = fields[9],
                        precinct = fields[10],

                        v20state = fields[11],
                        v21town = fields[12],
                        v21primary = fields[13],
                        v22general = fields[14],
                        v23town = fields[15],
                        voter_score = fields[16],
                        )
        
                result.save() # commit to database
                #print(f'Created result: {result}')

            except Exception as e:
                print(f"Skipped: {fields} due to error: {e}")
    
        print(f'Done. Created {len(Voter.objects.all())} Results.')

