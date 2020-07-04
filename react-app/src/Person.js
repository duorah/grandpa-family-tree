import React from 'react';
import { useQuery, useMutation } from 'react-apollo';
import { gql } from 'apollo-boost';

const QUERY_PERSONS = gql`
  query {
    persons {
      id,
      personId,
      givenname,
      surname,
      gender
    }
}
`;

const CREATE_PERSON = gql`
    mutation createPerson ($givenname: String!, $surname: String!, $gender: String!) {
        createPerson (givenname: $givenname, surname: $surname, gender: $gender){
            id,
            personId,
            givenname,
            surname,
            gender
        }
    }
`
export function PersonInfo() {
  // Polling: provides near-real-time synchronization with
  // your server by causing a query to execute periodically
  // at a specified interval
  const { data, loading } = useQuery(
    QUERY_PERSONS, {
      pollInterval: 2000 // refetch the result every 0.5 second
    }
  );

  // should handle loading status
  if (loading) return <p>Loading...</p>;

  return data.persons.map(({ id, personId, givenname, surname, gender}) => (
        <div key={id}>
            {id}:  {personId}  {givenname}  {surname}  {gender}
        </div>
  ));
}

export function CreatePerson() {
    let inputGivenName, inputSurname, inputGender;
    const [createPerson, { data } ] = useMutation(CREATE_PERSON);
    return (
        <div>
            <form
                onSubmit={e => {
                    e.preventDefault();
                    createPerson({ variables: {
                        givenname: inputGivenName.value,
                        surname: inputSurname.value,
                        gender: inputGender.value
                    }});
                    inputGivenName.value = '';
                    inputSurname.value = '';
                    inputGender.value = '';
                    window.location.reload();
               }}
            style = {{ marginTop: '2em', marginBottom: '2em' }}
           >
        <label>Given Name: </label>
        <input
            ref={node => {
                inputGivenName = node;
            }}
            style={{ marginRight: '1em' }}
        />
        <label>Surname: </label>
        <input
            ref={node => {
                inputSurname = node;
            }}
        />
        <label>Gender: </label>
        <input
            ref={node => {
                inputGender = node;
            }}
        />
        <button type="submit" style={{ cursor: 'pointer' }}> Add a User</button>

        </form>
     </div>
    );
}