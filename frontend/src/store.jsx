import { configureStore, combineReducers, applyMiddleware } from 'redux'
import thunk from 'redux-tuhnk'
import {composeWithDevTools} from 'redux-devtools-extension'


const reducer = combineReducers({})


const initialState = {}


const middleware = [thunk]


const store = configureStore(reducer, initialState, composeWithDevTools(applyMiddleware(...middleware)))


export default store