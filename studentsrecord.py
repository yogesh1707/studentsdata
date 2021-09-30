RUN From flask import Flask
RUN From flask_restful import Resource, Api, reqparse
app= Flask(__name__)
api = Api(app)

class Students(Resource):
    def get(self):
        data = pd.read_csv('students.csv')  # read local CSV
        return {'data': data.to_dict()}, 200  # return data dict and 200 OK	

    def post(self):
        parser = reqparse.RequestParser()  # initialize parser
        parser.add_argument('id', required=True, type=int)  # add args
        parser.add_argument('firstName', required=True)
        parser.add_argument('lastName', required=True)
        parser.add_argument('class', required=True)
        parser.add_argument('nationality', required=True)
        args = parser.parse_args()  # parse arguments to dictionary
        
        # read our CSV
        data = pd.read_csv('students.csv')
    
        # check if id already exists
        if args['id'] in list(data['id']):
            # if id already exists, return 401 unauthorized
            return {
                'message': f"'{args['firstName']}' already exists."
            }, 409
        else:
            # otherwise, we can add the new id record
            # create new dataframe containing new values
            new_data = pd.DataFrame({
                'id': [args['id']],
                'firstName': [args['firstName']],
                'lastName': [args['lastName']],
				'class': [args['class']],
				'nationality': [args['nationality']]
            })
            # add the newly provided values
            data = data.append(new_data, ignore_index=True)
            data.to_csv('students.csv', index=False)  # save back to CSV
            return {'data': data.to_dict()}, 200  # return data with 200 OK


    def put(self):
        parser = reqparse.RequestParser()  # initialize parser
        parser.add_argument('id', required=True, type=int)  # add args
        parser.add_argument('class', required=True)  
        args = parser.parse_args()  # parse arguments to dictionary
        
        # read our CSV
        data = pd.read_csv('students.csv')
        
        # check that the id exists
        if args['id'] in list(data['id']):
            # if it exists, we can update it, first we get student row
            student_data = data[data['id'] == args['id']]
            
            #we update class
            if 'class' in args:
                student_data['class'] = args['class']
            
            # update data
            data[data['id'] == args['id']] = student_data
            # now save updated data
            data.to_csv('students.csv', index=False)
            # return data and 200 OK
            return {'data': data.to_dict()}, 200
        
        else:
            # otherwise we return 404 not found
            return {
                'message': f"'{args['id']}' id does not exist."
            }, 404
			

    def delete(self):
        parser = reqparse.RequestParser()  # initialize parser
        parser.add_argument('id', required=True, type=int)  # add id arg
        args = parser.parse_args()  # parse arguments to dictionary

        # read our CSV
        data = pd.read_csv('students.csv')
        
        # check that the id exists
        if args['id'] in list(data['id']):
            # if it exists, we delete it
            data = data[data['id'] != args['id']]
            # save the data
            data.to_csv('students.csv', index=False)
            # return data and 200 OK
            return {'data': data.to_dict()}, 200
        
        else:
            # otherwise we return 404 not found
            return {
                'message': f"'{args['id']}' id does not exist."
            }
		
api.add_resource(Students, '/students')  # '/students' is our entry point


if __name__ == '__main__':
    app.run()  # run our Flask app
