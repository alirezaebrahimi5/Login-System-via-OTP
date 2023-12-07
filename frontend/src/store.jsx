import { createStore, combineReducers, applyMiddleware } from 'redux'
import thunk from 'redux-thunk'


const reducer = combineReducers({})


const initialState = {}


const store = createStore(reducer, initialState)


export default store