import { configureStore, combineReducers, applyMiddleware } from 'redux'
import thunk from 'redux-thunk'


const reducer = combineReducers({})


const initialState = {}


const store = configureStore(reducer, initialState)


export default store