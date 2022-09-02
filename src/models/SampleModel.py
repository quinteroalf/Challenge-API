from random import sample
from database.db import get_connection
from .entities.Sample import Sample


class SampleModel():

    @classmethod
    def get_Samples(self):
        try:
            connection = get_connection()
            samples = []

            with connection.cursor() as cursor:
                cursor.execute("SELECT first_name, last_name, company_name, address, city, state, zip, phone1, phone2, email, department FROM sample")
                resultset = cursor.fetchall()

                for row in resultset:
                    sample = Sample(row[0], row[1], row[2], row[3],row[4],row[5],row[6],row[7],row[8],row[9])
                    samples.append(sample.to_JSON())

            connection.close()
            return samples
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def get_sample(self, id):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM public.samples WHERE first_name = %s", (id,))
                row = cursor.fetchone()

                sample = None
                if row != None:
                    sample = sample(row[0], row[1], row[2], row[3])
                    sample = sample.to_JSON()

            connection.close()
            return sample
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def add_sample(self,  sample):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO public.sample
                                  (first_name, last_name, company_name, address, city, state, zip, phone1, email, department)
                                VALUES (%s, %s, %s, %s,%s,%s, %s, %s, %s,%s)""", 
                                (sample.first_name, sample.last_name, sample.company_name, sample.address, sample.city, sample.state, int(sample.zip), sample.phone1, sample.email, sample.department))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def update_sample(self, sample):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute(""" UPDATE public.sample SET last_name=%s, company_name=%s, address=%s, city=%s, state=%s, zip=%s, phone1=%s, email=%s, department=%s
                                WHERE first_name = %s""", ( sample.last_name, sample.company_name, sample.address, sample.city, sample.state, sample.zip, sample.phone1, sample.email, sample.department,sample.first_name))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows
        except Exception as ex:
            raise Exception(ex)

  
