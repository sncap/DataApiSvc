<template>
    <div align="center">
        <v-card max-width="96%">
            <!--dataSource-->
            <v-data-table
                    :headers="headers"
                    :items="dataSource"
                    sort-by="name"
                    :mobile-breakpoint='NaN'
                    :search="search"
                    class="elevation-1"
            >
                <template v-slot:top>
                    <v-toolbar flat color="white">
                        <v-toolbar-title>Data Source</v-toolbar-title>
                        <v-divider
                                class="mx-4"
                                inset
                                vertical
                        ></v-divider>
                        <v-spacer></v-spacer>
                        <v-text-field
                                v-model="search"
                                append-icon="mdi-magnify"
                                label="Search"
                                single-line
                                hide-details
                        ></v-text-field>
                        <v-spacer></v-spacer>
                        <v-dialog v-model="dialog" max-width="500px">
                            <template v-slot:activator="{ on }">
                                <v-btn color="primary" dark class="mb-2" v-on="on">New Data Source</v-btn>
                            </template>
                            <v-card>
                                <v-card-title>
                                    <span class="headline">{{ formTitle }}</span>
                                </v-card-title>

                                <v-card-text>
                                    <v-container>
                                        <v-row dense>
                                            <v-col cols="10">
                                                <v-text-field v-model="editedItem.name" label="Data Source name"></v-text-field>
                                            </v-col>
                                            <v-col cols="10">
                                                <v-text-field v-model="editedItem.db_url" label="DB URL"></v-text-field>
                                            </v-col>
                                            <v-col cols="10">
                                                <v-text-field v-model="editedItem.conn_max_cnt" label="Connection Max Count"></v-text-field>
                                            </v-col>
                                            <v-col cols="10">
                                                <v-text-field v-model="editedItem.conn_timeout" label="Connection Timeout"></v-text-field>
                                            </v-col>
                                            <v-col cols="10">
                                                <v-text-field v-model="editedItem.update_user" label="작성자"></v-text-field>
                                            </v-col>
                                            <v-col cols="10">
                                                <v-text-field v-model="editedItem.biz_dept" label="부서"></v-text-field>
                                            </v-col>
                                            <v-col cols="10">
                                                <v-text-field v-model="editedItem.biz_name" label="단위업무"></v-text-field>
                                            </v-col>
                                            <v-col cols="10">
                                                <v-text-field v-model="editedItem.user_id" label="사용자ID"></v-text-field>
                                            </v-col>

                                            <v-col cols="10">
                                                <v-text-field
                                                        label="Password *"
                                                        v-model="editedItem.passwd"
                                                        :type="show1 ? 'text' : 'password'"
                                                        :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
                                                        @click:append="show1 = !show1"
                                                ></v-text-field>
                                            </v-col>
                                            <v-col cols="10">
                                                <v-text-field v-model="editedItem.schema_name" label="Schema명"></v-text-field>
                                            </v-col>
                                        </v-row>
                                    </v-container>
                                </v-card-text>

                                <v-card-actions>
                                    <v-spacer></v-spacer>
                                    <v-btn color="blue darken-1" text @click="close">Cancel</v-btn>
                                    <v-btn color="blue darken-1" text @click="save">Save</v-btn>
                                </v-card-actions>
                            </v-card>
                        </v-dialog>
                    </v-toolbar>
                </template>
                <template v-slot:item.actions="{ item }">
                    <v-icon
                            small
                            class="mr-2"
                            @click="editItem(item)"
                    >
                        mdi-pencil
                    </v-icon>
                    <!--<v-icon
                            small
                            @click="deleteItem(item)"
                    >
                        mdi-delete
                    </v-icon>-->
                </template>
            </v-data-table>
        </v-card>
    </div>
</template>

<script>
    export default {
        name: "dataSource",
        data () { return {
            show1: false,
            dssearch: '',
            search: '',
            dsdialog: false,
            dialog: false,
            headers: [
                { text: 'Name', value: 'name'},
                { text: 'DB URL', value: 'db_url' },
                { text: 'Connection Max Count', value: 'conn_max_cnt' },
                { text: 'Connection Timeout', value: 'conn_timeout' },
                { text: 'Update User', value: 'update_user' },
                { text: '부서', value: 'biz_dept' },
                { text: '단위업무', value: 'biz_name' },
                { text: '사용자ID', value: 'user_id' },
                { text: '패스워드', value: 'passwd' },
                { text: 'Schema명', value: 'schema_name' },
                { text: 'DB Type', value: 'db_type' },
                { text: 'Actions', value: 'actions', sortable: false },
            ],
            dataSource: [],
            editedIndex: -1,
            editedItem: {
                name: '',
                db_url: '',
                conn_max_cnt: 0,
                conn_timeout: 0,
                update_user: '',
                biz_dept: '',
                biz_name: '',
                user_id: '',
                passwd: '',
                schema_name: '',
                db_type: ''
            },
            defaultItem: {
                name: '',
                db_url: '',
                conn_max_cnt: 0,
                conn_timeout: 0,
                update_user: '',
                biz_dept: '',
                biz_name: '',
                user_id: '',
                passwd: '',
                schema_name: '',
                db_type: ''
            },
            ds_headers: [
                { text: 'Name', value: 'name'},
                { text: 'API URL', value: 'api_url' },
                { text: 'SQL', value: 'sql' },
                { text: 'SQL Max Count', value: 'result_max_cnt' },
                { text: '응답대기시간', value: 'result_timeout' },
                { text: 'Actions', value: 'actions', sortable: false },
            ],
            dataService: [],
        }},
        computed: {
            formTitle () {
                return this.editedIndex === -1 ? 'New Data Source' : 'Edit Data Source'
            },
        },
        watch: {
            dialog (val) {
                val || this.close()
            },
        },
        methods: {
            editItem(item) {
                this.editedIndex = this.dataSource.indexOf(item)
                this.editedItem = Object.assign({}, item)
                this.dialog = true
            },
            dseditItem(item) {
                this.ds_editedIndex = this.dataService.indexOf(item)
                this.ds_editedItem = Object.assign({}, item)
                this.dsdialog = true
            },
            deleteItem(item) {
                const index = this.dataSource.indexOf(item)
                confirm('Are you sure you want to delete this item?') && this.dataSource.splice(index, 1)
            },
            close() {
                this.dsdialog = false
                this.dialog = false
                setTimeout(() => {
                    this.editedItem = Object.assign({}, this.defaultItem)
                    this.editedIndex = -1
                }, 300)
                setTimeout(() => {
                    this.ds_editedItem = Object.assign({}, this.ds_defaultItem)
                    this.ds_editedIndex = -1
                }, 300)
            },
            save() {
                if (this.editedIndex > -1) {
                    Object.assign(this.dataSource[this.editedIndex], this.editedItem)
                } else {
                    this.dataSource.push(this.editedItem)
                }
                if(!this.editedItem.schema_name) this.editedItem.schema_name = ""
                this.addUpdateDataSource(this.editedItem)
                this.close()
            },
            getDataSourcesInfo(){
                this.$axios.get('/cds/listallds',
                    {
                        headers: {
                            'x-cds-authentication': 'yjWq0Nv5bJOE3sZBZ4sGuK1KNHkD9KTX'
                        }
                    }
                ).then((response) => {
                    console.log(response.data)
                    this.dataSource = response.data
                }).catch(error => {
                    console.log({ error });
                })
            },
            addUpdateDataSource(params) {
                let data = this.editedItem
                this.$axios.get('/cds/ds_upsert', {
                    params: {
                        name: data.name,
                        db_url: data.db_url,
                        conn_max_cnt: data.conn_max_cnt,
                        conn_timeout: data.conn_timeout,
                        update_user: data.update_user,
                        biz_dept: data.biz_dept,
                        biz_name: data.biz_name,
                        user_id: data.user_id,
                        passwd: data.passwd,
                        schema_name: data.schema_name,
                        db_type: data.db_type
                    }}
                ).then((response) => {
                    console.log(response.data)
                }).catch(error => {
                    console.log({ error });
                })
            }
        },
        mounted() {
            this.getDataSourcesInfo()
        }
    }
</script>

<style scoped>

</style>
