import axios from 'axios';


export default {
    namespaced: true,
    state: {
        user: null,
        admin: null,
        refresh_token: null,
        endpoints: {
            obtainJWT: 'http://127.0.0.1:8000/api/token/',
            get_username: 'http://127.0.0.1:8000/api-user/getdata/'
        },
    },

    getters: {
        isAuthenticated (state) {
            return state.refresh_token && state.user
        },
        
        isAdmin (state) {
            return state.admin
        }
    },

    mutations: {
        SET_TOKENS (state, tokens) {
            if(tokens == null){
                axios.defaults.headers.common['Authorization'] = null

                localStorage.removeItem('access_token')
                localStorage.removeItem('refresh_token')

                localStorage.removeItem('credit_time')
                localStorage.removeItem('credit_sum')

                state.refresh_token = null;
            } else {
                localStorage.setItem('access_token', tokens.access)
                localStorage.setItem('refresh_token', tokens.refresh)
                
                state.refresh_token = tokens.refresh
            }
        },
        SET_USER (state, data) {
            if(data == null){
                state.user = null
                state.admin = null
            } else {
                state.user = data.username
                if (data.is_admin) {
                    state.admin = data.is_admin
                }
            }
        }
    },

    actions: {
        async obtainTokens ({ dispatch, state }, credentials) {
            let response = await axios.post(state.endpoints.obtainJWT, credentials)
            return dispatch('attempt', response.data)
        },

        async attempt({ commit, state }, tokens) {

            if (tokens.access) {
                commit('SET_TOKENS', tokens)
            }

            if (!state.refresh_token) {
                return
            }

            try {
                let response = await axios.get(state.endpoints.get_username)
                commit('SET_USER', response.data)

            } catch (error) {
                commit('SET_TOKENS', null);
                commit('SET_USER', null);
            }
        },

        logOut ({ commit }) {
            commit('SET_TOKENS', null);
            commit('SET_USER', null);
        }
    },
}
