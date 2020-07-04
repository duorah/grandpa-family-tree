import React from 'react';
import ApolloClient from 'apollo-boost'
import { ApolloProvider } from '@apollo/react-hooks'
import { PersonInfo , CreatePerson } from './Person'

import './App.css';

const client = new ApolloClient({
    uri: 'http://localhost:8000/graphql/', // graphql server
})

const App = () => (
    <ApolloProvider client={client}>
    <div style={{
      backgroundColor: '#00652158',
      display: 'flex',
      justifyContent:'center',
      alignItems:'center',
      height: '10vh',
      flexDirection: 'column',
    }}>
    <h2>GRanD Family Tree App </h2>
    <text> A GraphQL, React and Django Application </text>
    </div>
    <div>
        <CreatePerson/>
    </div>
    <div style={{
      backgroundColor: '#00000028',
      display: 'flex',
      justifyContent:'right',
      alignItems:'left',
      height: '100vh',
      flexDirection: 'column',
    }}> <PersonInfo/> </div>
    </ApolloProvider>
)

export default App;
