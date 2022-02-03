<template>
    <div align="center">
        <v-card max-width="96%">
            <v-data-table
                    :headers="ds_headers"
                    :items="dataService"
                    sort-by="api_url"
                    :mobile-breakpoint='NaN'
                    :search="dssearch"
                    class="elevation-1"
            >
                <template v-slot:top>
                    <v-toolbar flat color="white">
                        <v-toolbar-title>Data Service</v-toolbar-title>
                        <v-divider
                                class="mx-4"
                                inset
                                vertical
                        ></v-divider>
                        <v-spacer></v-spacer>
                        <v-text-field
                                v-model="dssearch"
                                append-icon="mdi-magnify"
                                label="Search"
                                single-line
                                hide-details
                        ></v-text-field>
                        <v-spacer></v-spacer>
                        <v-dialog v-model="dsdialog" max-width="500px">
                            <template v-slot:activator="{ on }">
                                <v-btn color="primary" dark class="mb-2" v-on="on">New Data Service</v-btn>
                            </template>
                            <v-card>
                                <v-card-title>
                                    <span class="headline">{{ formTitle }}</span>
                                </v-card-title>

                                <v-card-text>
                                    <v-container>
                                        <v-row dense>
                                            <v-col cols="10">
                                                <v-text-field dense v-model="ds_editedItem.name" label="Data Service API name"></v-text-field>
                                            </v-col>
                                            <v-col cols="10">
                                                <v-text-field dense :disabled="ds_editedIndex > -1" v-model="ds_editedItem.api_url" label="DS API URL"></v-text-field>
                                            </v-col>
                                            <v-col cols="10">
                                                <v-textarea dense v-model="ds_editedItem.sql" label="SQL"></v-textarea>
<!--                                                <v-text-field v-model="ds_editedItem.sql" label="SQL"></v-text-field>-->
                                            </v-col>
                                            <v-col cols="10">
                                                <v-text-field dense v-model="ds_editedItem.result_max_cnt" label="Result Max Count"></v-text-field>
                                            </v-col>
                                            <v-col cols="10">
                                                <v-text-field dense v-model="ds_editedItem.result_timeout" label="응답대기시간"></v-text-field>
                                            </v-col>
                                            <v-col cols="10">
                                                <v-text-field dense v-model="ds_editedItem.cache_timeout" label="캐쉬사용시간"></v-text-field>
                                            </v-col>
                                        </v-row>
                                    </v-container>
                                </v-card-text>

                                <v-card-actions>
                                    <v-spacer></v-spacer>
                                    <v-btn color="blue darken-1" text @click="close">Cancel</v-btn>
                                    <v-btn color="blue darken-1" text @click="dssave">Save</v-btn>
                                </v-card-actions>
                            </v-card>
                        </v-dialog>
                    </v-toolbar>
                </template>
                <template v-slot:item.actions="{ item }">
                    <v-icon
                            small
                            class="mr-2"
                            @click="dseditItem(item)"
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
        name: "DataService",
        data () { return {
            dssearch: '',
            search: '',
            dsdialog: false,
            ds_headers: [
                { text: 'Name', value: 'name'},
                { text: 'API URL', value: 'api_url' },
                { text: 'SQL', value: 'sql' },
                { text: 'SQL Max Count', value: 'result_max_cnt' },
                { text: '응답대기시간', value: 'result_timeout' },
                { text: '캐쉬사용시간', value: 'cache_timeout' },
                { text: 'Actions', value: 'actions', sortable: false },
            ],
            dataService: [],
            ds_editedIndex: -1,
            ds_editedItem: {
                name: '',
                api_url: '',
                sql: '',
                result_max_cnt: 0,
                result_timeout: 0,
            },
            ds_defaultItem: {
                name: '',
                api_url: '',
                sql: '',
                result_max_cnt: 0,
                result_timeout: 0
            },
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
            dssave() {
                if (this.ds_editedIndex > -1) {
                    Object.assign(this.dataService[this.ds_editedIndex], this.ds_editedItem)
                } else {
                    this.dataService.push(this.ds_editedItem)
                }
                this.addUpdateDataService(this.ds_editedItem)
                this.close()
            },
            getDataServiceInfo(){
                this.$axios.get('/cds/listallsql',
                    {
                        headers: {
                            'x-cds-authentication': 'yjWq0Nv5bJOE3sZBZ4sGuK1KNHkD9KTX'
                        }
                    }
                ).then((response) => {
                    console.log(response.data)
                    this.dataService = response.data
                }).catch(error => {
                    console.log({ error });
                })
            },
            addUpdateDataService(params) {
                this.$axios.get('/cds/sql_upsert',
                        {params}
                ).then((response) => {
                    console.log(response.data)
                }).catch(error => {
                    console.log({ error });
                })
            }
        },
        mounted() {
            this.getDataServiceInfo()
        }
    }
</script>

<style scoped>

</style>
